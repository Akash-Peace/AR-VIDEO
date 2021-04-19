import cv2, numpy as np
def plot(fg_image, aruco_value_top_left, aruco_value_top_right, aruco_value_bottom_right, aruco_value_bottom_left):
    img = cv2.VideoCapture(0)
    src = cv2.VideoCapture(fg_image)
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    aruco_para = cv2.aruco.DetectorParameters_create()
    prev_frame = [1]
    init_aruco_detected = 0
    while img.isOpened():
        _, frame = img.read()
        ret, src_frame = src.read()
        if ret:
            corners, ids, rej = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_para)
            if (len(corners) != 4) and init_aruco_detected == 0:
                cv2.imshow("AR_Video", frame)
            else:
                try:
                    if (len(corners) != 4) and init_aruco_detected == 1:
                        dst_mat = prev_frame[0]
                    else:
                        init_aruco_detected = 1
                        ids = ids.flatten()
                        ref_pts = []
                        for i in (aruco_value_top_left, aruco_value_top_right, aruco_value_bottom_right, aruco_value_bottom_left):  # 923, 1001, 241, 1007
                            j = np.squeeze(np.where(ids == i))
                            corner = np.squeeze(corners[j])
                            ref_pts.append(corner)
                        refPtTL, refPtTR, refPtBR, refPtBL = ref_pts
                        dst_mat = [refPtTL[0], refPtTR[1], refPtBR[2], refPtBL[3]]
                        dst_mat = np.array(dst_mat, np.int32)
                        prev_frame[0] = dst_mat
                    src_h, src_w = src_frame.shape[:2]
                    img_h, img_w = frame.shape[:2]
                    src_matrix = np.array([[0, src_h], [0, 0], [src_w, 0], [src_w, src_h]])
                    cv2.fillConvexPoly(frame, dst_mat, 0)
                    homography, _ = cv2.findHomography(src_matrix, dst_mat)
                    warped = cv2.warpPerspective(src_frame, homography, (img_w, img_h))
                    combined = cv2.add(frame, warped)
                    cv2.imshow("AR_Video", combined)
                except:
                    cv2.imshow("AR_Video", frame)
        else:
            src.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img.release()