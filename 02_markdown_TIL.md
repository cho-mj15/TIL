## git  폴더 생성과 진입

> - 처음 git을 활용하기 위해선 폴더 생성과 그 폴더로 진입을 해야한다.

1. 폴더 생성

```bash
$ git mkdir aaa(폴더명)
```

2. 폴더 진입

```bash
$ cd aaa(폴더명)
```

## `git init`로 git 시작하기

```bash
$ git init 
-> 폴더위치 뒤에 (master)가 생성됨
```

## 파일 작업과 그 후 `commit` 하기

> 다른 언어를 작업한 후 git으로 저장하고 싶은 경우에는 작업한 파일을 git저장소 폴더에 이동시킨 후 `add`와 `commit`커맨드를 실행한다.

- `add`와 `commit`커맨드 실행방법

```bash
$ git add 파일명
$ git commit -m "구분할 수 있는 아무단어"
```

## 자신의 원격 저장소 (github)를 git에 불러 온 후 저장

- 원격 저장소 불러오기

```bash
$ gir remote add (저장소명) [github repository 주소]
```

- 파일을 원격 저장소에 올리기

```bash
$ git push (저장소명) master
```

## github에 저장된 작업파일을 다른 위치의 pc에서 작업할때

> 작업했던 파일을 저장해 놓고 다른 곳에서 다시 작업하고 싶을때 (ex> 회사에서 작업하던 것을 집에서) 는 `clone`커맨드를 활용한다.

- `clone`커맨드와 github의 원격 저장소 url을 입력한다.

```bash
$ git clone [저장된 파일이 있는 github 원격 저장소 주소]
```



## github 저장소에 있는 파일을 현재 컴퓨터 파일로 불러올때

> 원격 저장소엔 있지만 현재 사용중인 pc에 파일이 없고,이 파일을 pc로 불러오고 싶다면 `pull`커맨드를 활용한다.

```bash
$ git pull (저장소명) master
```

##  git에 입력한 원격 저장소의 이름과 주소를 확인할때

```bash
$ git remote 
$ git remote -v
```

## git에 입력한 원격 저장소 이름을 바꾸고 싶을때

``` bash
$ git remote rename (현재 저장소명) (바꿀 저장소명)
```

