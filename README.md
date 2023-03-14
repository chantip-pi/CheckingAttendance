# Checking attendance

ระบบเช็คชื่ออัตโนมัติ

---

## การติดตั้ง

**จำเป็นต้องติดตั้ง Conda ก่อน สามารถดูวิธีการติดตั้งได้ที่ https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages  
  
ถ้าหากติดตั้ง Conda แล้วให้รันคำสั่งด้านล่างเพื่อทำการสร้าง Environment และติดตั้ง Package

```bash
# Create environment
conda create -n attendance python=3.8
conda activate attendance
# Install package
pip install scikit-learn scipy opencv-python mtcnn tqdm pandas numpy keras_facenet imutils matplotlib pytest-shutil 
```

## โครงสร้าง

* ``videos/`` เป็นโฟลเดอร์สำหรับเก็บวิดีโอที่ใช้ในการ train model ซึ่งจะถูกแยกกลายเป็นรูปภาพ
* ``dataset/`` เป็นโฟลเดอร์ที่เก็บข้อมูลรูปภาพที่ถูกสร้างมา (โดยจะถูกสร้างหลังจากมีการ Generate รูปภาพจากวิดีโอแล้ว)
  * ``dataset/train/`` เป็นโฟล์เดอร์ที่เก็บรูปภาพที่ใช้สำหรับ train
  * ``dataset/val/`` เป็นไฟล์เดอร์ที่เก็บรูปภาพที่ใช้สำหรับ validate
  * ``dataset/test/`` เป็นไฟล์เดอร์ที่เก็บรูปภาพที่ใช้สำหรับ validate
* ``sheets/`` เป็นโฟลเดอร์สำหรับเก็บ sheet ที่ได้จากเช็คชื่อในแต่ละรอบ (โดยจะถูกสร้างหลังจากมีการ generate รูปภาพจากวิดีโอแล้ว)

## วิธีการใช้งาน
