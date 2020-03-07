# QLineEdit
- 基本功能：输入单行文本

- setPlaceholderText(): 设置当文本框没有输入时的显示

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
- 自己搜掩码

    
    