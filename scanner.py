import cv2
from pyzbar.pyzbar import decode
import pandas as pd
from datetime import datetime

class EmployeeScanner:
    def capture_qr(self):
        # This function captures employee attendance details and saves them in xlsx file.
        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            decoded_objects = decode(frame)
            # get scanned card id
            for obj in decoded_objects:
                id = obj.data.decode('utf-8')
                print(f"EmpId: {id}")
                # create dataframe including card id, date and time of attenance
                data = {"EmployeeID": [id, ], "Date": [datetime.now().date(), ], "Time": [datetime.now().time(), ]}
                df = pd.DataFrame(data)
                df.to_excel("attendance_report.xlsx", sheet_name='Employee Attendance Report', index=False)

            cv2.imshow("Employee Code Scanner", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Card Scanned")

    def search_record(self):
        # the function reads employee details from xls file and prints them
        df = pd.read_excel('attendance_report.xlsx')
        print(df)
