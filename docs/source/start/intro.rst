前言
==================
    该文档写于2024年9月。

在开始之前
----------------

《Unix网络编程》书上的源码存放在
`Github仓库 <https://github.com/unpbook/unpv13e>`_
中。

克隆该项目到本地。我这里使用的linux系统。


.. code-block:: bash

    $ git clone https://github.com/unpbook/unpv13e.git

根据代码仓库的README文档，执行以下操作。

.. code-block:: bash

    $ cd unpv13e/
    $ ./configure
    $ cd lib/
    $ make

make后在unpv13e目录下生成了libunp.a静态库，将libunp.a移动到
/usr/lib或/usr/lib64下都可。

然后将unpv13e/lib/unp.h以及unpv13e/config.h这
两个头文件移动到/usr/local/include下，并将unp.h里的
:code:`#include	"../config.h"` 改为 
:code:`#include	"config.h"`。
也可以自己建立个项目文件夹，将这两个头文件拖进去就行。



编译第一个示例程序
----------------

.. code-block:: bash

    $ cd unpv13e/intro/
    $ gcc daytimetcpcli.c -o client

在编译后可能会出现err_quit和err_sys未定义的情况。
这是因为这两个函数实现是被封装在《Unix环境高级编程》的
源代码里面的，因此需要前往
`apue源代码网站 <http://www.apuebook.com/code3e.html>`_
下载源码。
解压源代码


.. code-block:: 

    $ tar -zxvf src.3e.tar.gz
    $ cd apue.3e


找到apue.3e/include/apue.h以及apue.3e/lib/error.c，
其中error.c包含了err_quit和err_sys等函数的实现，
apue.h包含这些函数的声明，因此需要将unp.h头文件包含
:code:`#include "apue.h"`, 并将error.c包含进
apue.h头文件中。

.. note::

   将apue.h和error.c放入自己项目文件夹中，或是移动到
   /usr/local/include下。
