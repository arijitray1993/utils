import cv2
import torch
import numpy as np
import pdb


def _detect_black_bars_from_video(frames, blackbar_threshold=16, max_perc_to_trim=.2):
    ## from Merlot reserve code base by Rowan Zellers. 
    """
    :param frames: [num_frames, height, width, 3]
    :param blackbar_threshold: Pixels must be this intense for us to not trim
    :param max_perc_to_prim: Will trim 20% by default of the image at most in each dimension
    :return:
    """

    # Detect black bars
    has_content = frames.max(axis=(0, -1)) >= blackbar_threshold
    h, w = has_content.shape

    y_frames = np.where(has_content.any(1))[0]
    if y_frames.size == 0:
        print("Oh no, there are no valid yframes")
        y_frames = [h // 2]

    y1 = min(y_frames[0], int(h * max_perc_to_trim))
    y2 = max(y_frames[-1] + 1, int(h * (1 - max_perc_to_trim)))

    x_frames = np.where(has_content.any(0))[0]
    if x_frames.size == 0:
        print("Oh no, there are no valid xframes")
        x_frames = [w // 2]
    x1 = min(x_frames[0], int(w * max_perc_to_trim))
    x2 = max(x_frames[-1] + 1, int(w * (1 - max_perc_to_trim)))
    return y1, y2, x1, x2



def get_video_frames(vidcap, fps=None, interval=None):
    
    v_fps = vidcap.get(cv2.CAP_PROP_FPS)

    if v_fps==0:
        return None
    

    
    if interval!=None:
        start_time_ms, stop_time_ms = interval
    else:
        start_time_ms = 0
        frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count==0:
            return None
        try:
            stop_time_ms = frame_count*1000/v_fps
        except:
            pdb.set_trace()
    
    count = 0
    success = True

    while success and vidcap.get(cv2.CAP_PROP_POS_MSEC) < start_time_ms:
        success, image = vidcap.read()

    frames = []
    if fps!=None:
        skip_length = max(round(v_fps/fps), 1)
    i_cnt = 0
    while success and vidcap.get(cv2.CAP_PROP_POS_MSEC) <= stop_time_ms:
        i_cnt+=1
        success, image = vidcap.read()
        if fps!=None:
            if i_cnt%skip_length!=0:
                continue;
        

        #pdb.set_trace()
        if success:
            frames.append(image)
    
    frames = np.stack(frames)
    
    blackbar_threshold=32 
    max_perc_to_trim=.20
    y1, y2, x1, x2 = _detect_black_bars_from_video(frames, blackbar_threshold=blackbar_threshold,
                                                   max_perc_to_trim=max_perc_to_trim)
    frames = frames[:, y1:y2, x1:x2]
    
    formatted_frames = [] #format in the way torch wants stuff. 
    for image in frames:
        image = torch.tensor(image) # this is h,w,ch
        if len(image.shape)<3:
            image = image[None, :,:] # this is 1, h, w
            image = image.repeat(3,1,1) # this is 3, h, w
        else:
            image = image.permute(2,0,1) #this is ch, h, w
        
        formatted_frames.append(image)


    return formatted_frames