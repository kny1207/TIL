# GIT

GIT은 분산형버전관리시스템(DVCS)이다.

소스코드 형상 관리 도구로, 코드의 이력을 관리할 수 있따.



## Git 로컬 저장소 활용하기

git은 ` repository(저장소) `로 각각 프로젝트를 관리한다.



## 0. 기본설정

* TIL 폴더 오른쪽에서 Git bash here 누르고 열기!
* 숨김폴더에 .git폴더 있는 상태에서만 들어가야 제대로 작동한다.

Git에서 이력을 남기기 위해 작성자(author) 정보를 추가한다. 매 컴퓨터에서 최초로 한 번만 설정하면 된다.

``` bash
$ git config --global user.name {유저네임}
( $ git config --global user.name NayeonKim127 )
$ git config --global user.email {이메일}
( $ git config --global user.email rkgh0411@gmail.com )
$ $ git config --global -l 치면 내 정보가 나오게 된다.
```

* 일반적으로 {유저네임}, {이메일}에는 github 정보를 넣는다.

* 개발자 폰트는 '고정 폰트'



## 1. 저장소 생성

```bash
$ git init
Initialized empty Git respository in C:/Users/student/Desktop/.새TIL/.git/
(master) $
```



## 2. add

커밋 대상 파일을 staging area로 이동 시킨다.

즉, 이력을 남길 파일을 담아 놓는 것이다.

.은 현재 디렉토리(폴더)를 뜻한다

``` bash
$ git add .		   # 현재 디렉토리 모두 stage
$ git add git.md   # 내가 원하는 특정 파일만 올리는 것
$ git add images/  # 특정 폴더만 stage
: 이력을 남기는 것. 출석체크하려고 사진찍기 위해 무대에 올라가는 것과 같은
```

항상 git status명령어를 통해 상태를 확인하자

:  지금 잘 하고 있는지 문제가 있는지 단계별로 확인할 수있다.

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   "\353\247\210\355\201\254\353\213\244\354\232\264\355\231\234\354\232\251\353\262\225.md"

```

## 3. commit

git에서 이력을 남기기 위해서는 커밋을 진행 == 확정을 짓는다.

```bash
$ git commit -m 'Git 기초'
[master (root-commit) ed876a4] Git 기초
 1 file changed, 118 insertions(+)
 create mode 100644 "\353\247\210\355\201\254\353\213\244\354\232\264\355\231\234\354\232\251\353\262\225.md"

```

* 이력을 확인하기 위해서는 git log를 활용한다.

```bash
$ git log
commit ed876a48976142cb4d9882f40b9839883dee167e (HEAD -> master)
Author: NayeonKim127 <rkgh0411@gmail.com>
Date:   Thu Dec 5 12:34:55 2019 +0900

    Git 기초
```



## Git 원격 저장소 활용하기

### 0. 기본 설정

원격 저장소를 생성한다. (예 - github)



## 1. 원격 저장소 등록

origin 이라는 이름으로 해당 url을 원격 저장소로 등록! 최초에 한번만 하면 된다.

```bash
$ git remote add origin https://github.com/NayeonKim127/TIL.git
```

```bash
$ git remote -v  # 원격 저장소 목록
origin  https://github.com/NayeonKim127/TIL.git (fetch)
origin  https://github.com/NayeonKim127/TIL.git (push)
```



## 2. 원격 저장소 push

앞으로 변경되는 사항이 있으면 항상 add, commit, push를 진행한다.

```bash
$ git push -u origin master
Everything up-to-date
Branch 'master' set up to track remote branch 'master' from 'origin'.
```



* [강사님 정리](https://github.com/edutak/TIL-a)

  : https://github.com/edutak/TIL-a

