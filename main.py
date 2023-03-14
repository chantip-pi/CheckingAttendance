from modules.sheet_generator import SheetGenerator
from modules.image_generator import video_to_image, make_shuffle_dataset
from face_recognition.camera import open_camera

print('=== NaHong Attendance System ===')

subject = input('Enter subject name:')

# Instanciate SheetGenerator
sheet = SheetGenerator(subject, 'sheets')

while(True):
    print('Please select an option: ')
    print('(1) Convert video to image')
    print('(2) Train model')
    print('(3) Start attendance')
    print('(4) Close attendance')
    print('================================')
    
    option = int(input('Option: '))
    
    if (option == 1):
        print('Converting ...')
        video_to_image('videos', 'images')
        print('Converted!')
        
        print('Splitting ...')
        make_shuffle_dataset('images')
        print('Splitted!')
    if (option == 2):
        pass
    if (option == 3):
        pass
    if (option == 4):
        break

# Save file
sheet.close()