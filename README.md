# Personal Knowledge Repository
The Goal is something simple and the data is written in your own words. This is not a dumping ground for things you've collected, bookmarks or notes that are verbatim copies of learning modules. The goal is to have a clear index of useful references with minimal overhead, no cost and no security risk. 

This is A collection of templates highlighting my code that I've utilized to solve specific problems. Also a collection of my notes and tutorials that I have created for myself over the years of working in tech. Placing them here, organizes them and keeps them in a place that can't be lost by either time, moving jobs, or from physically losing a notebook or laptop.

## Why and How to Use
### Why? 
- After leaving a job you can't keep any of the scripts or knowlege
    - Creating templates from the completed working scripts allows you to carry that knowledge forward and avoid having to start over every time.
- After stepping away from a completed project it can take time to reaquaint yourself with the code and find the notes attached to it
    -Collecting notes here on different use cases or templates can get you up to spead quickly on the project and improvements you were working on
- Changing computers and having to export all bookmarks and notes trashes the organization and makes it difficult to find the important documents to refer back to years later
    -Having an external location eliminates misplacement and having to restart the organization system
- While having a public facing blog can be a great way to share knowledge and keep a it for yourself, not everyone wants to go through the effort to make notes readable by others, nor do they want that information public. 

### How?
- Each section is personally written by yourself. 
    - This helps with knowledge retention as well as to help you know where you've placed information since you played an acitve role in putting the informatoin there. You can't remember something you didn't participate in or something you blinded dumped somewhere. 
- Each item is an abstraction of its original, wether that be a script or your notes on a learning module. The abstraction highlights the important parts and where to go to to find more information on a subject. 
- Each item is a guide to help you remember your thought process and enhance your skills and knowledge. Its also a place to help you prevent re-inventing wheels you've already invented or solving the same problems you have already solved before. 

## How its organized
Three categories: 
- Code Templates
- Notes 
- and self made Tutorials. 

Notes about the code templates are made with the same name as the template and are stored in the same folder as the template. Should the knowledge base grow large, a seperate folder will be created. The Template notes will mark problem areas on the top, followed by short reasonings, and finished with where I was looking next to improve the code. 

There is also a seperate place for general notes, not tied to a script template. Could include links to blog post that I liked or found helpful, learning material or notes on classes I've taken. This can also include pictures of physical notes as a stop gap until they are transcribed into a digital format. 

Lastly, a folder for Tutorials I've made either describing scripts and their functions or for explaining how to do something specific, especially when I haven't found a tutorial publicly or the tutorials I found did not cover the use case I encountered. 

## What it should not contain
It explicitly should not contain exact copies of scripts that were made for a company, it should not contain secrets of any kind, and it should not include any data that would be classified as private or propiatary by a company or person other than yourself. ESPECIALLY if this knowledge repository is hosting on the github cloud EVEN MORE SO if you have made the repository public facing. 

No
   - **Secrets**
   - **Company data**
   - **Propriatary data**
   - **Personal Identifiable Information**

## This is a resource for you and to help you in your career. Use this template to create something for yourself to use, organize it to how you like. :) 


# To Get Started

### 1. Download the file structure and examples

1. Download the Knowledge base template 
2. Rename the folder to your chosen knowledge base name

Next is the MdWiki part to make the markdown files readable in a web browser

### 2. MdWiki installation

1. Download the .zip file from the latest release on the [Download page](https://dynalon.github.io/mdwiki/#!download.md), which will direct you to github and then you click on the latest .zip file.
2. Unpack the .zip file
3. Copy the mdwiki.html file to the top level directory of the Knowledge base folder
4. Change the name of the mdwiki.html file to index.html (this will then automatically load the index.md file that you have created for your knowledge base homepage)
5. Lastly, adde a navigation file or any other simple feature highlighted on the mdwiki quickstart page [Here](https://dynalon.github.io/mdwiki/#!quickstart.md) 

Next is creating a simple python server to serve up the website hosted locally!

### 3. Simple python server for self hosting

1. In a terminal, navigate to the Knowledge base folder and execute a simple python server
```python
python3 -m http.server --bind 127.0.0.1  8080
```
2. Open up a browser and travel to localhost:8080 to view the knowledge base!

### 4. Lastly make the knowledge base your own

- With a code or text editor, edit and all the files to the knowledge base and adding references to those files in the index.md file and thats it!
- The webiste rendering can be customized and added to. For example a navigation bar can be customized with drop down menus, Change the name of the branding and more. Check out Mwiki for more information on how to do that. 
- The knowledge base template is a guideline to get you started, feel free to change the directory structure or templates as you see fit. *HOWEVER* Never host the server to the public internet using the simple server above. It is not a secure server at all. For more about that [here](https://docs.python.org/3/library/http.server.html#security-considerations) is the man page for the server talking about the security flaws.

## Notes

Mwiki is used to render the index.md file into something a server can read. By adding the mwiki html file to the high level folder, which is renamed to index.html, a simple server can now read and render the index.md file. Allowing the knowledge base to come more alive and be a searchable reference. Would also allow it to be hosted on a small server on a local network, that is not accessible via the internet.

# Websites and blog post references

This blog post is what got me started on creating this Knowledge base template:
https://dev.to/adam_b/a-personal-git-repo-as-a-knowledge-base-wiki-j51

https://dynalon.github.io/mdwiki/#!index.md 

https://docs.python.org/3/library/http.server.html#security-considerations

https://docs.python.org/3/library/http.server.html# 