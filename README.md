LabelImage:
    所有文件的编码方式使用utf-8
    增加图片亮度调节滑块
    增加图片大小调节滑块
    亮度调节下一张图片任然保持
    显示/隐藏所有标签集中在一个按钮
    选择自定义的classes去标记图片
    连续替换label，将连续的几张图片的第一个标记改为同一类
    自动保存模式下，只要canvas发生变化，都会自动保存
    单个类别标记模式
    显示标记的文字描述
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
    亮度调节：调节当前图片的亮度
    Size调节：调节当前图片的大小
    margin pixel：标记框向外延伸的大小
    turn page：自定义翻页
    label add white：以白色显示标记文本
    参考亮度：显示当前图片的亮度
    Use default label：使用设定类别进行标记
    continue replace Label：对已经标记的图片进行批量修改，每张图片只会修改其中一个标记框
    openPrevLabelImg：打开上一张有标记的图片
    openNextLabelImg：打开下一张有标记的图片

快捷键:
    quit: Ctrl+Q
    open: Ctrl+O
    opendir: Ctrl+Shift+O
    changeSavedir: Alt+R
    openPrevImg: Z
    openNextImg: X
    openPrevLabelImg:Alt+X
    openNextLabelImg:Alt+Z
    turnPageNextImg:W
    save: Ctrl+S
    close: Alt+Q
    create: ALT+D
    edit: ALT+E
    copy: Ctrl+C
    delete: Delete
    displayAll: Ctrl+H
