# 贡献规范

[English version](CONTRIBUTE.md)

## 导引

首先感谢您关注 EduData 并致力于让其变得更好！
在您开始贡献自己的一份力之前，需要注意以下几点：

1. 如果您希望我们实现新的功能。
   - 可以在通过 issue 来告诉我们您想要的功能，我们将及时展开讨论设计和实现。
   - 一旦我们一致地认为这个计划不错，那么您可以期待新的功能很快就可以与您见面。
2. 如果您想要对于某个未解决问题的 issue 提供解决性意见或 bug 修复。
   - 可以先在 [EduData issue list](https://github.com/bigdata-ustc/EduData/issues) 中搜索您的问题。
   - 之后，选择一个具体问题和评论，来提供您的解决性意见或者 bug 修复。
   - 如果对于具体的 issue，您需要更多的细节，请向我们咨询。
3. 您想添加新的数据分析或增加新的数据集

一旦您实现并已经测试过了你的想法或者是对于 bug 的修复，请通过 Pull Request 提及到到 [EduData](https://github.com/bigdata-ustc/EduData) :
1. 首先fork此仓库到你的分支下
2. 对代码进行修改。注意：我们强烈建议你遵守我们的 [commit格式规范](CONTRIBUTE_CH.md#关于Commit的格式)
3. 通过代码测试，测试覆盖度达到100%，例子可见[此处](tests)
4. 通过Pull Request 提及到到 [EduData](https://github.com/bigdata-ustc/CDM) 。注意：我们提供了一个标准的PR请求模板，你需要认真完成其中的信息，一个标准且规范的PR可参考[此处](https://github.com/bigdata-ustc/EduData/pull/37)

以下是对于不同贡献内容的有用建议：

### 添加新的数据集

目前，我们仅支持通过使用我们提供的接口从[BaseData](http://base.ustc.edu.cn/data/)网站进行数据下载

如果你想要添加一份新的数据集，您可以首先通过issue提出数据上传请求，之后完成如下两件事：

* 在 [download_data.py](Edudata/Dataset/download/data/download_data.py) 的 `URL_DICT` 添加新的键值对
* 运行 `pytest` 测试数据下载是否正常

### 添加新的数据分析

### 代码注释风格

请使用 Numpy 代码注释风格：

```
function 的功能

    Parameters
    ----------
    变量名 1: 类型, 是否 optional
       描述
    变量名 2: 类型, 是否 optional
       描述
    ...

    Returns
    -------
    变量名: 类型
       描述

    See Also (可选)
    --------
    类似 function: 类似 function 的功能

    Examples (可选)
    --------
    >>> 举例怎么用
```

### 关于Commit的格式

#### commit format

```
[<type>](<scope>) <subject>
```

#### type
- `feat`：新功能（feature）。
- `fix/to`：修复 bug，可以是 Q&A  发现的 bug，也可以是自己在使用时发现的 bug。
   - `fix`：产生 diff 并自动修复此问题。**适合于一次提交直接修复问题**。
   - `to`：只产生 diff 不自动修复此问题。**适合于多次提交**。最终修复问题提交时使用 `fix`。
- `docs`：文档（documentation）。
- `style`：格式（不影响代码运行的变动）。
- `refactor`：重构（即非新增功能，也不是修改 bug 的代码变动）。
- `perf`：优化相关，比如提升性能、体验。
- `test`：增加测试。
- `chore`：构建过程或辅助工具的变动。
- `revert`：回滚到上一个版本。
- `merge`：代码合并。
- `sync`：同步主线或分支的 bug。
- `arch`: 工程文件或工具的改动。

#### scope (可选)

scope 是用于说明 commit 影响的范围，比如<u>数据层</u>、<u>控制层</u>、<u>视图层</u>等等，视项目不同而不同。

例如在 Angular，可以是 location，browser，compile，compile，rootScope， ngHref，ngClick，ngView等。如果你的修改影响了不止一个scope，你可以使用`*`代替。

#### subject (必须)

subject 是 commit 目的的简短描述，不超过50个字符。

结尾不加句号或其他标点符号。

#### Example

- **[docs] update the README.md**

```sh
git commit -m "[docs] update the README.md"
```

## FAQ

问题: 我已经在本地仔细地测试了代码，并通过了代码检查，但是在 CI 步骤时却报错？
回答: 这个问题可能是两个原因造成： 
1. 在线的 CI 系统与您自己本地系统有差别；
2. 可能是网络原因造成的，如果是可以通过 CI 的日志文件查看。