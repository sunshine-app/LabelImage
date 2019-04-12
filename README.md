# LabelImage
LabelImage:
    所有文件的编码方式使用utf-8
    增加图片亮度调节滑块
    增加图片大小调节滑块
    亮度调节下一张图片任然保持
    显示/隐藏所有标签集中在一个按钮
    选择自定义的classes去标记图片
    连续替换label，将连续的几张图片的第一个标记改为同一类
    自动保存模式下，只要canvas发生变化，都会自动保存
    增加文件列表提示

运行方式：
    python labelImg.py

环境依赖：
    Python3 + PyQt5 + Pillow + lxml

说明：
    predefined_classes.txt在项目data目录下
    txt文本文档使用标准utf-8格式，即无BOM的utf-8
    在类别存在中文的情况下，一定要使predefined_classes.txt的格式为无BOM的utf-8格式
    使用之前需要重置所有，删除以前的配置依赖，重新运行生成新的配置
    在自动保存模式下最后一张图片需要手动保存
    可以使用单个类别模式，或者使用Use default label

快捷键:
    quit: Ctrl+Q
    open: Ctrl+O
    opendir: Ctrl+Shift+O
    changeSavedir: Alt+R
    openNextImg: Alt+N
    openPrevImg: Alt+P
    save: Ctrl+S
    close: Alt+Q
    create: Ctrl+N
    edit: Ctrl+E
    copy: Ctrl+C
    delete: Delete
    displayAll: Ctrl+H
