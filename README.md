# Checking attendance

ระบบเช็คชื่ออัตโนมัติ

---

## การติดตั้ง

**จำเป็นต้องติดตั้ง Conda ก่อน สามารถดูวิธีการติดตั้งได้ที่ https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages  
  
ถ้าหากติดตั้ง Conda แล้วให้รันคำสั่งด้านล่างเพื่อทำการสร้าง Environment และติดตั้ง Package  
  
สร้าง environment

```sh
conda create -n attendance python=3.8
conda activate attendance
```

ติดตั้ง package

```sh
pip install scikit-learn scipy opencv-python mtcnn tqdm pandas numpy keras_facenet imutils matplotlib pytest-shutil 
```

## โครงสร้าง

* ``videos/`` เป็นโฟลเดอร์สำหรับเก็บวิดีโอที่ใช้ในการ train model ซึ่งจะถูกแยกกลายเป็นรูปภาพ
* ``dataset/`` เป็นโฟลเดอร์ที่เก็บข้อมูลรูปภาพที่ถูกสร้างมา (โดยจะถูกสร้างหลังจากมีการ Generate รูปภาพจากวิดีโอแล้ว)
  * ``dataset/train/`` เป็นโฟลเดอร์ที่เก็บรูปภาพที่ใช้สำหรับ train
  * ``dataset/val/`` เป็นไฟลเดอร์ที่เก็บรูปภาพที่ใช้สำหรับ validate
  * ``dataset/test/`` เป็นไฟลเดอร์ที่เก็บรูปภาพที่ใช้สำหรับ validate
* ``sheets/`` เป็นโฟลเดอร์สำหรับเก็บ sheet ที่ได้จากเช็คชื่อในแต่ละรอบ (โดยจะถูกสร้างหลังจากมีการ generate รูปภาพจากวิดีโอแล้ว)

## การเตรียมข้อมูล

วิดีโอที่ใช้สำหรับการ train จะเป็นวีดิโอหน้าตรงของบุคคล โดยใช้ framerate 30 fps ในการถ่าย ความยาว 7-8 วินาที นามสกุลไฟล์ ``.mp4`` ตัวอย่างวิดีโอ ``example_video.mp4``

## วิธีการใช้งาน

นำไฟล์วิดีโอที่เตรียมไว้มาใส่ในโฟลเดอร์ ``videos/`` โดยชื่อไฟล์ของวิดีโอ นั้นจะคือ id ของคน คนนั้นที่ปรากฎบนไฟล์ชีท

ทำการรันไฟล์ ```main.py``` โดยใช้ terminal (จำเป็นที่จะต้อง activate environment ก่อน)  

```sh
conda activate attendance
python main.py
```

เมื่อรันแล้วจะพบกับ

```text
=== NaHong Attendance System ===
Enter subject name:
```

โดยในส่วนนี้ให้ใส่ชื่อวิชาที่เช็คชื่อโดยชื่อวิชาเป็นคำนำหน้าของชื่อไฟล์ sheet ของการเช็คชื่อ จากนั้นก็จะพบเมนู  

```text
Please select an option: 
(1) Convert video to image
(2) Train model
(3) Start attendance
(4) Close attendance
================================
Option:
```

ถ้าหากต้องการใช้งานตัวเลือกไหนให้พิมพ์ตัวเลือกนั้นจากนั้นกด Enter (พิมพ์แต่ตัวเลข)

โดยแต่ละตัวเลือกจะมีการทำงานดังนี้

1. ทำการแปลงวิดีโอให้กลายเป็นรูป และทำการแยกแบ่งข้อมูลเป็น train validation test
2. ทำการ train โมเดล ในขั้นตอนนี้เราจะได้ไฟล์ model_v1.pkl มา
3. ทำการเริ่มเช็คชื่อโดยจะมีการเปิดกล้อง (ในการเช็คชื่อนั้นให้พยายามนำหน้ามาใกล้กล้องเพื่อความแม่นยำ)
4. ทำการปิดการเช็คชื่อ ในขั้นตอนนี้จะทำการปิดกล้อง และสร้างไฟล์ชีทของการเช็คชื่อ
