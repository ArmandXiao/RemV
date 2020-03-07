# QLineEdit
- 基本功能：输入单行文本

- setPlaceholderText(): 设置当文本框没有输入时的显示

- setMaxLength(int): 限制最大输入长度

- setReadOnly(Boolean)
### 常用事件
- textChanged

 ###Echo mode : 设置回显模式 
1. Normal

2. NoEcho: 输入的文本不显示 感觉敲了半天啥也没输入

3. Password

4. PasswordEchoOnEdit: 编辑时显示，不编辑就变成password形式

- 添加模式的方法: setEchoMode( **QLineEdit.Normal** ) e.g.

    
##QLineEdit 校验器 ：限制控件的输入
- *setValidator 与 QlineEdit组件捆绑*

- QIntValidator     检测输入是否为整数
    - 可配合 setRange()来限定范围
    
- QDoubleValidator  浮点数
    - 可配合 setRange()来限定范围
    - setDecimal 设置精度
    
- QRegExValidator   检测字符串是否满足提供的正则
    - import QRegEx
    - setRegEx(reg)
    
## QLineEditMask 掩码: 限制控件输入
用掩码限制QLineEdit控件的输入
>   A    ASCII字母字符是必须输入的(A-Z、a-z) \
    a    ASCII字母字符是允许输入的,但不是必需的(A-Z、a-z)\
    N    ASCII字母字符是必须输入的(A-Z、a-z、0-9)\
    n    ASII字母字符是允许输入的,但不是必需的(A-Z、a-z、0-9)\
    X    任何字符都是必须输入的\
    x    任何字符都是允许输入的,但不是必需的\
    9    ASCII数字字符是必须输入的(0-9)\
    0    ASCII数字字符是允许输入的,但不是必需的(0-9)\
    D    ASCII数字字符是必须输入的(1-9)\
    d    ASCII数字字符是允许输入的,但不是必需的(1-9)\
    #    ASCI数字字符或加减符号是允许输入的,但不是必需的\
    H    十六进制格式字符是必须输入的(A-F、a-f、0-9)\
    h    十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)\
    B    二进制格式字符是必须输入的(0,1)\
    b    二进制格式字符是允许输入的,但不是必需的(0,1)\
    >    所有的字母字符都大写\
    <    所有的字母字符都小写\
    !    关闭大小写转换\
    \    使用"\"转义上面列出的字符\

    
    