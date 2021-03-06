# RemV  :thumbsup: <br/> ![](https://img.shields.io/badge/license-GPL3.0-000000.svg)![](https://img.shields.io/badge/platform-Windows-green.svg)![](https://img.shields.io/badge/version-v1.1-red.svg)
**Note：This open source project follows [GNU General Public License v3.0](LICENSE), and the right of authorship is comopletely held by Lingao, Xiao.**  
**注意: 这个开源项目遵从 [GUN通用公开许可协议 v3.0](GUN通用公开许可协议)，著名权被 *肖凌奥* 全权持有.**
***
**:point_right:[中文版](README.md) :point_left:**
***
- This software can run on multi-platform.
<div id="Catalog"></div>  

## Latest Release Version
- Version 1.1

## Catalog
 

  [1.Why do I choose *RemV*](#First)  
  
  [2. Functions](#Second)  
  
  [3. **Download**](#Third)  
  
  [4. How to set up](#Fourth)  
  
  [5. How to use](#Fifth)  
    
  [7. Added Functions of new releases](#Seventh)
  -   [7.1. Project preview](#Sixth)  
  
  [8. APIs](#Eighth)
  
  [9. Special Acknowledgement](#Ninth)
  
<div id="First"></div>  

## 1. Why do I choose *RemV*
[Go to Catalog](#Catalog)

> RemV is a software that helps to build long-term memory of vocabularies.
#### Distinguishing from other softwares, **RemV** has three sections of memorizing.
1. Memorizing
2. Confirmation
3. Quiz 

The combination of these three rounds helps to fasten the foundation.
#### Why do I create this software in PC clients instead of mobile ones.
- Moblie clients are hard to check spellings of words. A relative tiny keyboard 
increases the probablities of making mistakes. As a result, 
it is a waste of time about reciting words that have been already mastered.
- People have hard time paying attention to the software only in moblie clients.
- Most of mobile sotfwares do not have a way to upload their own vocabulary list.
#### Compared with books, what are the **pros** of RemV. 
- Experiening a period of reciting words, I do think using a book makes people sleepy. 
Especially for learner whose native language is not English.
  - Continuous interaction prevents sleepness.
- Books cannot automatically collects wrong-spelling words.

<div id="Second"></div>

## 2. Functions 

[Go to Catalog](#Catalog)

## General
- [x] Upload your own vocabulary list or book (*.xlsx)
    > I have my own book to uplaod. I don't want to **always** recite the same books.
- [x] **Quick Enter of words**
    > Words are summarized on books, and entering words in excels are so compliated and time-consuming!
    - Don't worry, *RemV* has quick enter function.
    - In RemV, you can ONLY enter the WORD itself; part of speech and corresponding meaning can be auto-filled with web-crawler.
    - You don't even need to open the excel.
    - RemV will also create the excel in `Rem/lib/res/word_repository`
- [x] Books are auto-seperated into lesson which contains at most 20 words.
- [x] Record the progess
- [x] Record the cumulative words you have remembered. When the number gets bigger, you will have sense of achievement. I swear. o(\*￣▽￣\*)ブ
- [x] Double Click to Remove a book. Note: the excel still remains on your computer.
- [x] Sentences from great people

### Memorizing Scene
- [x] Pronounce words
- [x] Acquire part of speech and corresponding meanings of each POS online.
- [x] Able to hide/show the meanings of words.
- [x] Frequency of word use
- [x] Tags of words
- [x] Corresponding pictures of words
- [x] Prefix and Suffix of words


### Quiz Scene
- [x] Words in quiz scene are given randomly.
- [x] Hint of the word is shown, including the length of the word, the spaces, and the start letter.
- [x] Real time spelling-cheking, which avoids unnecessary mistakes.
- [x] Rollback of wrong-spelling words.
- [x] All words that you have spelled incorrectly will be written in `Error Book`.
<div id="Third"></div>  

## 3. Download

[回到目录](#Catalog)

### Windows: https://github.com/ArmandXiao/RemV/releases/tag/v1.0
  - 1.0 Version is now released.
  - **`RemV.exe`** is the executable software.
  - **[WordBook Repository](#WordRepository)** is the library where I integrate the resources of popular book.
    - Download the ones that you need.
    - Then upload in **RemV**
    - ENJOY your journey.
### MacOS: Stay tuned...

<div id="Fourth"></div>  

## 4. How to set up

[Go to Catalog](#Catalog)  

1. Download `RemV_setup-Beta-Version.exe`
2. According to setup information, install it on your computer.
3. Open `RemV` file
4. Scroll down, find `RemV.exe`
5. Double click `RemV.exe`
6. *Optional*：Right click `RemV.exe` -> created a shortcut -> cut the shortcut on to your Desktop -> Rename
7. If there is Dialog jumping out, that means you have successfully run.

**PLEASE, DO NOT MOVE `RemV.exe` TO OHTER FILE**  

<div id="Fifth"></div>  

## 5. How to use  

[Go to Catalog](#Catalog)  

<div id="WordRepository"></div>  

1. Download books that you need.
    - link: *https://share.weiyun.com/53OJHOc* Code: t5qsb1  
2. Click the button on top-right corner -> upload the book you have downloaded.
3. Click the name of the book
4. Click a lesson
5. Click Memorize on right part ("RECOMMANDED")
    - Tip 
    ![image](image/tip_1.jpg)  
    
    - **From top to bottom, the functions are Show Meaning and Translate, respectively.**  

6. Click Quiz on the right part, to start a quiz directly. ("**NOT** RECOMMANDED")
7. Complete!

<div id="Seventh"></div>  

## 7. Added Functions of new releases  
[Go to Catalog](#Catalog)  
### v1.1
- **整体布局修改：大小调整**
- Frequency of word use
- Picture of words, if they have
- Prefix and suffix
- Tags of words
- Sentences from great people
- ![image](PyQt5_GUI/version_previews/Preview-v1.1/English/preview_1.jpg)
- ![image](PyQt5_GUI/version_previews/Preview-v1.1/English/preview_2.jpg)
- ![image](PyQt5_GUI/version_previews/Preview-v1.1/English/preview_3.jpg)
### v1.0
- run in multi-threading
- ![image](PyQt5_GUI/version_previews/Preview-v1.0/English/preview_1.png)
- ![image](PyQt5_GUI/version_previews/Preview-v1.0/English/preview_2.png) 
<div id="Sixth"></div>  

## 7.1. Project Preview.

[Go to Catalog](#Catalog)
### This is the preview for Aplha Version
- ![image](PyQt5_GUI/version_previews/Preview-Beta/preview_1.jpg) 
- ![image](PyQt5_GUI/version_previews/Preview-Beta/English/preview_2.png) 
- ![image](PyQt5_GUI/version_previews/Preview-Beta/English/preview_3.png) 
- ![image](PyQt5_GUI/version_previews/Preview-Beta/English/preview_4.png) 
- ![image](PyQt5_GUI/version_previews/Preview-Beta/English/preview_5.png) 
- ![image](PyQt5_GUI/version_previews/Preview-Beta/English/preview_6.png) 
- ![image](PyQt5_GUI/version_previews/Preview-Beta/English/preview_7.png) 

<div id="Eighth"></div>   

## 8. APIs
[Go to Catalog](#Catalog)

- **YouDao Dictionary: translation，part of speech，phonetic symbol** 
- **YouDao Dictionary voice: American pronunciation，British pronunciation**
- **Cg Dictionary: Frequency of word use**
- **OuLu Dictionary: Pictures，Tags of words**

<div id="Ninth"></div>   

## 9. Special Acknowledgement
[Go to Catalog](#Catalog)

- The inspiration of RemV icon came from ***杨其霖, Gary Young***
