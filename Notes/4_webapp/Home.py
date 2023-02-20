import streamlit as st

st.set_page_config(page_title="Home",
                    layout='wide',
                    page_icon='./images/para.jpg')

st.title("Object Detection Web App cf. YOLOv5")
st.caption('このアプリでは物体認識を体験することができます')
st.balloons()

# Content
st.markdown("""
### このアプリは、画像から物体を検出します
- 画像から 20 個のオブジェクトを自動的に検出
- [Click here for Detail of Object Model](https://github.com/ultralytics/yolov5)

モデルが検出するオブジェクトです
1. Person
2. Car
3. Chair
4. Bottle
5. Sofa
6. Bicyle
7. Horse
8. Boat
9. Motor Bike
10. Cat
11. Tv Monitor
12. Cow
13. Sheep
14. Aeroplane
15. Train
16. Dining Table
17. Bus
18. Potted Plant
19. Bird
20. Dog

            """)