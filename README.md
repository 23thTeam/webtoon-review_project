# 웹툰어스(Webtoon us)
**📖 웹툰 리뷰 웹사이트**
- 웹툰을 검색하고, 웹툰 리뷰를 작성하여 웹툰 별, 유저 별로 작성한 리뷰를 볼 수 있는 사이트입니다.

<br/>
<br/>

## 브로셔
<br/><img width="800" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/b9930d6c-aaf5-4a51-9855-3edda4a5a5e1">

## 로고
<br/><img width="200" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/c16125f2-6d88-4c35-bc87-e6e80165c8e3">

<br/>
<br/>

## ✅ 배포한 사이트
[웹툰어스(Webtoon us)](https://baegeunwoo2.pythonanywhere.com/)

<br/>

# 👋 팀 소개
|이름|깃허브|
|:--:|:--|
| **👑 김노을 (조장)** | [👾 Github @noeulgim](https://github.com/noeulgim) |
| **😄 배근우** | [👾 Github @zz6331300zz](https://github.com/zz6331300zz) |
| **😎 정은화** | [👾 Github @summereuna](https://github.com/summereuna) |

<br/>

## 🤙🏻 협업을 위한 규칙
- Gather에 모여 9 to 9 로 각자 맡은 기능을 구현하는데 집중
- 점심 시간 12:00 - 13:00
- 저녁 시간 18:00 - 19:00
- 어려움이 있을 땐 팀원 들에게 공유
- 기술 매니저 님과의 질문 타임은 보통 19:30 이후에 진행

<br/>

## 🙌🏻 담당 기능
|이름|담당 기능|
|:--:|:--|
| 김노을 | - 전체 유저 리뷰 조회<br/>- 유저별 리뷰 조회 |
| 배근우 | - 리뷰 DB 작업<br/>- 리뷰 Form 작업 및 리뷰 생성<br/>- 리뷰 삭제, 업데이트 (추가 기능 구현 중)<br/>- 배포 |
| 정은화 | - 외부 웹툰 API로 웹툰 DB생성 작업<br/>- 전체 웹툰 및 상세 페이지 조회<br/>- 웹툰 별 리뷰 조회<br/>- 웹툰 검색 기능 |

<br/>
<br/>
<br/>

# 프로젝트 내용
## 1. ⏰ 프로젝트 기간
2024년 6월 12일 ~ 6월 14일 (3일)

<br/>

## 2. ⚒️ 사용 기술
- Jinja2, HTML, JavaScript, Bootstrap, CSS
- Python, Flask
- SQLite, SQLAlchemy
- [korea-webtoon-api](https://github.com/HyeokjaeLee/korea-webtoon-api)

<br/>

## 3. ⚙️ 설계
### 3-1. API 설계
|기능|Method|URL|request(요청)|response(응답)|
|:--|:--|:--|:--|:--|
홈페이지|GET|`/`|||
서비스 별 웹툰 조회|GET|`/webtoon`|{<br/>"id": id,<br/>"webtoon_id": webtoon_id,<br/>"title": title,<br/>"author": author,<br/>"url": url,<br/>"img": img,<br/>"service": service,<br/>"update_days": update_days,<br/>"fan_count": fan_count,<br/>"search_keyword": search_keyword<br/>}|서비스 별, 요일 순으로 정렬된 웹툰 리스트|
검색 시 GET 사용할 경우 혼동 생기므로,<br/>POST 로 받아 서치로 리디렉션|POST|`/webtoon`|query={keyword}|검색 서비스 별 웹툰 리스트|
검색한 웹툰 조회|GET|`/webtoon/search`|query={keyword}|입력된 keyword, service에 대해 서비스 별, 날짜 순으로 정렬된 웹툰 리스트|
웹툰 상세 페이지<br/>및 웹툰 별 리뷰 조회|GET|/webtoon/<webtoon_id>|query={webtoon_id}|웹툰 id와 맞는 웹툰 데이터와 리뷰 리스트|
리뷰 작성|POST|`/webtoon/create`|{<br/>’username’: username,<br/>’review’: review,<br/>’webtoon_id’: webtoon_id,<br/>}|사용자가 form에서 작성한 리뷰 데이터|
전체 유저 리뷰 조회|GET|`/user`|.|유저별 전체 유저 리뷰 리스트|
유저 개인 별 리뷰 조회|GET|`/user/<username>`|username=username|유저 별 리뷰 리스트|
리뷰 삭제|DELETE/POST|`/webtoon/delete`<br/>→ 변경<br/>`/review/delete`|webtoon_id|삭제할 해당 리뷰 데이터|
리뷰 수정|UPDATE/POST||||
- 리뷰 삭제
    - 기존에 Webtoon 테이블에 리뷰내용 정보가 있었는데 Review 테이블로 리뷰내용을 바꾸면서 `/user/delete`로 변경함.
    - 삭제 및 업데이트 기능은 구현 중…
- (🚨 REST Full API로 작성을 위해 엔드 포인트 수정 필요)
- 
<br/>

### 3-2. 와이어 프레임 설계
<br/><img height="400" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/ad1eb353-5f4f-44a7-bc77-417fb628a566">
- 기존에 작성한 와이어 프레임으로 결과와 조금 다릅니다.

<br/>

### 3-3. ERD 설계
<br/><img height="400" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/e9de5ddb-f290-4bde-853f-4db4e59f3a00">
- (🚨 Webtoon 데이터에 Review 데이터를 1대N 관계로 매핑 하지는 못함)

<br/>
<br/>

## 4. ⚒️ 구현 기능
### 4-1. 기본 CRUD
#### 4-1-1. **Create(생성)**
- Webtoon data: 서버 초기화 시 외부 API에서 불러와서 딱 한 번 생성
- `/webtoon/create`, Review data: 유저가 form으로 작성 시 생성 (🚨 REST Full API로 작성을 위해 엔드 포인트 수정 필요)
#### 4-1-2. **Read(읽기)**
- `/webtoon`
  - 서비스 별 전체 Webtoon DB 조회, 날짜 순 정렬
- `/webtoon/search`
  - 쿼리로 받은 keyword로 keyword가 포함된 Webtoon DB 조회
- `/webtoon/<webtoon_id>`
  - id 별 Webtoon DB 조회
- `/user`
  - 유저 별 Review DB 조회
- `/user/<username>`
  - 유저 별 Webtoon DB 조회
#### 4-1-3. **Update(갱신)**
- 리뷰 수정 기능 (🚨 REST Full API로 작성 필요)
#### 4-1-4. **Delete(삭제)**
- 리뷰 삭제 기능 (🚨 REST Full API로 작성 필요)

<br/>

### 4-2. 기능 설명
#### 4-2-1. 웹툰 (은화)
1. **홈페이지 (`/`)**
   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/b556e9ed-ab45-4c5b-a8f6-99c895307744/image.png">
   - 홈페이지 구성
   - 로고 및 이미지는 무료 템플릿 사이트 이용

3. **웹툰별 리뷰 페이지 (`/webtoon`)**
   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/c35ceb21-8f1b-4867-8ae1-de474dd088ce/image.png">
   - 웹툰 서비스별, 날짜 순서대로 Webtoon DB를 조회하여 data 처리
   - SQLAlchemy의 case()를 사용하여 조건 별로 컬럼에 숫자 값을 부여하여 순서 처리 가능하게 함
     - Webtoond의 update_days 컬럼이 영문 문자열로 되어 있었기 때문에, "월~일/연재 종료/매일+" 순으로 숫자 값을 부여하여 웹툰 데이터 조회 시 오름 차순으로 정렬할 수 있게 함
        ```python
        # 웹툰 데이터 요일 정렬 순서
        update_days_order = case(
            (Webtoon.update_days == 'mon', 1),
            (Webtoon.update_days == 'tue', 2),
            (Webtoon.update_days == 'wed', 3),
            (Webtoon.update_days == 'thu', 4),
            (Webtoon.update_days == 'fri', 5),
            (Webtoon.update_days == 'sat', 6),
            (Webtoon.update_days == 'sun', 7),
            (Webtoon.update_days == 'finished', 8),
            (Webtoon.update_days == 'naverDaily', 9)
        )
        ```
    
   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/0272d96f-cabc-483a-85f8-45cf6e964c9b/image.png">
   - 웹툰 서비스, 연재일 값을 조건부로 한국어로 변경
   - (예시) 연재일 값 변경 코드
     - (방법 1) jinja2로 구현: if elif else 문
        ```html
            <span id="updateDay" class="badge text-bg-dark ms-1">
                                    {% if webtoon.update_days == "mon" %} 월 {% elif
                                    webtoon.update_days == "tue" %} 화 {% elif
                                    webtoon.update_days == "wed" %} 수 {% elif
                                    webtoon.update_days == "thu" %} 목 {% elif
                                    webtoon.update_days == "fri" %} 금 {% elif
                                    webtoon.update_days == "sun" %} 토 {% elif
                                    webtoon.update_days == "finished" %} 완결 {% else %}
                                    매일+ {% endif %}
                                  </span>
        ```
            
     - (방법 2) JavaScript로 구현: switch 문 
        ```js
            <script>
                  function getDayKorean(updateDays) {
                    let result = "";
                    switch (updateDays) {
                      case "mon":
                        result = "월요일";
                        break;
                      case "tue":
                        result = "화요일";
                        break;
                      case "wed":
                        result = "수요일";
                        break;
                      case "thu":
                        result = "목요일";
                        break;
                      case "fri":
                        result = "금요일";
                        break;
                      case "sat":
                        result = "토요일";
                        break;
                      case "sun":
                        result = "일요일";
                        break;
                      case "finished":
                        result = "완결";
                        break;
                      case "naverDaily":
                        result = "매일+";
                        break;
                    }
                    return result;
                  }
            
                  document.addEventListener("DOMContentLoaded", (event) => {
                    const updateDaySpan = document.getElementById("updateDay");
                    const updateDay = updateDaySpan.getAttribute("data-update-day");
                    const koreanDay = getDayKorean(updateDay);
                    updateDaySpan.textContent = koreanDay;
                  });
            
                </script>
            ```
            
   - **Webtoon을 제공하는 service에 따른 버튼 색상 변경**
     - 네이버: 초록색
     - 카카오, 카카오페이지: 노란색
   - 검색 시 템플릿 혼동을 피하기 위해 검색 keyword를 POST로 먼저 받아 /search로 리디렉션
     - (코드)
        ```python
            @app.route("/webtoon", methods=['GET', 'POST'])
            def webtoon():
                # 서비스 별, 날짜 순서대로 Webtoon data 반환
                def get_by_service_webtoon_db(service):
                    service = Webtoon.query.filter_by(service=service).order_by(update_days_order).all()
                    webtoon_list = [webtoon.to_dict() for webtoon in service]
                    return webtoon_list
            
                context = {
                    "naver": get_by_service_webtoon_db(service="naver"),
                    "kakao": get_by_service_webtoon_db(service="kakao"),
                    "kakaoPage": get_by_service_webtoon_db(service="kakaoPage"),
                }
            
                # 검색 시 GET 사용할 경우 혼동 생기므로, POST 로 받아 서치로 리디렉션 먼저하기
                if request.method == 'POST':
                    keyword = request.form.get('keyword')
                    return redirect(url_for('search', keyword=keyword))
            
                return render_template("webtoon.html", data=context)
            ```
            
5. **검색 기능 (`/webtoon/search`)**
   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/0b2d0655-c593-4dc3-bf29-6811cef20778/image.png">
   - 포워딩 받은 keyword를 파라미터로 받아 데이터 처리
     - (코드)
        ```python
            @app.route("/webtoon/search")
            def search():
                # GET 메소드로 검색 결과 받아오기
                keyword = request.args.get('keyword')
            
                # 입력된 keyword, service에 대해 날짜순으로 웹툰 db 조회
                def get_by_keyword_filter_by_service_webtoon_db(keyword, service):
                    webtoons = Webtoon.query.filter(Webtoon.search_keyword.like(f'%{keyword}%')).filter_by(service=service).order_by(update_days_order).all()
                    webtoon_list = [webtoon.to_dict() for webtoon in webtoons]
                    if webtoon_list:
                        return webtoon_list
                    else:
                        return None # 검색 결과 없는 경우 예외 처리를 위해 None 반환
                
                if keyword:
                    context = {
                        "naver" : get_by_keyword_filter_by_service_webtoon_db(keyword, "naver"),
                        "kakao" : get_by_keyword_filter_by_service_webtoon_db(keyword, "kakao"), 
                        "kakaoPage" : get_by_keyword_filter_by_service_webtoon_db(keyword, "kakaoPage")
                    }
            
                    data = {
                        "webtoons" : context,
                        "keyword": keyword,
                    }
            
                    return render_template("search.html", data=data)
                # 키워드 없으면 원래대로 리디렉션
                else:
                    return redirect(url_for('webtoon'))
            
            ```

   <br/><img width="500" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/2b0eb610-83dd-4b0c-8aae-5aa1f1f4c2cb">
   - **예외 처리**
     - 검색 결과가 없는 경우 None을 반환하여 if else 구문으로 예외 처리
     - 데이터가 없을 때도 에러가 발생하지 않도록 작업
   - **유저 인터페이스 개선**
     - 데이터가 없는 경우 찾는 웹툰이 없다고 표시

6. **웹툰 상세 페이지 (`/webtoon/<webtoon_id>`)**
   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/d8fd12d9-bbf6-4681-9ec2-195d813d0967/image.png">
   - **웹툰 id 별 Webtoon db 조회**
     - 파라미터로 받은 id 값으로 웹툰 db에서 데이터를 검색하여 웹툰 상세 페이지의 jinja템플릿으로 보내어 각 id 파라미터에 따른 웹툰 상세 정보 조회
     - (코드)
         ```python
            @app.route("/webtoon/<webtoon_id>")
            def webtoonDetail(webtoon_id):
                # api 데이를 순회해서 id 같은 웹툰 찾기
                webtoon = Webtoon.query.filter_by(webtoon_id=int(webtoon_id)).first()
            
                # 리뷰 데이터: webtoon_id 필터해서 가져오기
                reviews = Review.query.filter_by(webtoon_id=int(webtoon_id)).all()
                webtoon_review_list = [review.to_dict() for review in reviews]
                
                # 테스트용 데이터
                # webtoon_review_list = []
                # review1 = {
                #     'username': '유저 이름',
                #     'title': '리뷰 제목',
                #     'text': '리뷰 텍스트 리뷰 텍스트 리뷰 텍스트 테스트'
                # }
                # webtoon_review_list.append(review1)
                # webtoon_review_list.append(review1)
                # webtoon_review_list.append(review1)
                # webtoon_review_list.append(review1)
                # webtoon_review_list.append(review1)
                # webtoon_review_list.append(review1)
                # webtoon_review_list.append(review1)
            
                # 웹툰 상세 데이터, 웹툰 전체 리뷰 데이터
                data = {
                    "webtoon_detail": webtoon,
                    "webtoon_review_list": webtoon_review_list,
                }
            
                return render_template("webtoonDetail.html", data=data)
            ```

   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/6cf98564-4b72-453b-9ae4-121322ceebc6/image.png">
   - **웹툰 id 별 전체 사용자 Review db 조회**
     - 웹툰에 대한 모든 사용자 리뷰에 대한 Review db를 조회하여 상세 페이지로 data를 보내고, 상세 페이지에서 사용자가 이 웹툰에 대해 리뷰한 글 조회
   - **jinja템플릿의 for in 구문을 사용하여 reviews 배열 순회**

   <br/><img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/ccd973b9-e4fb-459e-b18f-745f5395347f/image.png">
   <img width="500" alt="screenshot" src="https://velog.velcdn.com/images/summereuna/post/08dc6a5a-6a4b-4489-8bd5-34e30117a7a2/image.png">
   - **예외 처리**
     - None 값을 반환하는 데이터의 컬럼에 대해 if else 구문으로 예외 처리
     - 데이터가 없을 때도 에러가 발생하지 않도록 작업
   - **유저 인터페이스 개선**
     - 데이터가 없는 경우 어울리는 설명 추가

<br/>

#### 4-2-2. 리뷰 (근우)
1. **리뷰 생성**

2. **리뷰 삭제 (기능 구현 중)**

3. **리뷰 수정 (기능 구현 중)**
   
<br/>

#### 4-2-3. 유저 (노을)
1. **전체 유저 리뷰 페이지 (`/user`)**
   <br/><img width="500" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/58f58018-4d9e-4ce4-bfd4-38f9f3886bc8">
   - 모든 리뷰와 웹툰을 가져와 해당하는 웹툰 리뷰를 찾아서 데이터를 생성하고 'user.html' 템플릿으로 렌더링
      ```python
      # 배열 생성
      webtoon_reviews = []
      
      for review in reviews:
          for webtoon in webtoons:
              # 리뷰와 웹툰이 일치하면 추가
              if review.webtoon_id == webtoon.webtoon_id:
                  webtoon_reviews.append({
                      'username': review.username,
                      'review': review.review,
                      'title': webtoon.title,
                      'author': webtoon.author,
                      'url': webtoon.url,
                      'img': webtoon.img,
                      'service': webtoon.service,
                      'webtoon_id': webtoon.webtoon_id
                  })
      ```

   - **유저 리스트를 가져와 중복된 유저 이름 처리**
      ```jsx
      //username들이 있는 태그 가져오기
      userList = document.getElementsByClassName('username');
      		//반복문을 사용해서 username 다음 인덱스에 같은 username이 있으면 .append()로 추가
          for(var i = 0; i < userList.length; i++){
            for(var j = i + 1; j <= userList.length; j++){
                if(userList[j].children[0].innerText == userList[i].children[0].innerText){
                        userList[i].append(userList[j].children[1]);
                        userList[j].remove();
                        j = i;
                    }
                }
              }
      ```

2. **유저별 리뷰 페이지 (`/user/<username>`)**
   <br/><img width="500" alt="screenshot" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/a7e98c18-e3a8-4596-94ee-f5d1c2c3d629">
   - 특정 유저 이름을 기반으로 해당 유저의 리뷰를 필터링하고, 해당하는 웹툰 리뷰를 찾아서 데이터를 생성하고 'user.html' 템플릿으로 렌더링
      ```python
      filter_list = Review.query.filter_by(username=username).all()
      ...
      ```

<br/>
<br/>

## 5. 🚀 트러블슈팅
### 5-1. 외부 API 관련 서버 에러
#### 문제
- 웹툰 정보를 활용한 웹 사이트를 구성하기 위해 [korea-webtoon-api](https://github.com/HyeokjaeLee/korea-webtoon-api)를 사용하여 웹툰 정보를 가져와 화면에 렌더링하고, 사용자의 리뷰 작성 데이터에 추가하는 등의 작업을 하고 있었습니다.
- 로컬 환경에서는 아무런 문제 없이 잘 진행되어 프로덕트 환경에서도 문제가 없는지 확인하기 위해 테스트를 진행하게 되었습니다.
- 배포 테스트 중, Pythonanyware을 통해 배포한 프로덕트 환경에서는 웹툰 API를 받아오지 못하는 **Server error: MaxRetryError, Proxy error 가 발생**했습니다.
  <br/>
  <img width="500" alt="server error" src="https://github.com/23thTeam/webtoon-review_project/assets/58466648/7d216fe5-f60f-4c33-9641-7ed8b3c50124">

#### 문제 원인
- Pythonanyware는 보안을 위해 서버에서 크롤링 할 수 있는 웹사이트를 제한하고 있었습니다.
- 무료 사용자는 Pythonanyware의 **whitelist**에 적힌 도메인으로만 서버에 접근할 수 있기 때문에, 프로덕트 환경에서는 웹툰 API를 사용하여 작업할 수 없게 되었습니다.
- 참고: [Pythonanyware: Allowlisted sites for free users](https://www.pythonanywhere.com/whitelist/)

#### 해결 방법
- 서버 초기화 시 웹툰 API 에서 모든 웹툰 data 받아와 Webtoon DB에 저장하여 사용하는 것으로 데이터를 처리하는 방법을 전환했습니다.
- Webtoon DB 생성하는 코드는 딱 한 번만 실행하여 DB를 완성해 두면 되기 때문에, 서버 초기화 시 Webtoon DB를 생성한 후 DB를 생성하는 코드는 주석 처리 하였습니다.
  ```python
  # # 서버 시작 전 웹툰 api 받아와 DB에 저장하여 사용
  # # 이유: python anywhere 가 불분명한 api 접근 지원하지 않으므로 500 server error, proxy error 발생
  # def create_webtoon_db():
  #     webtoon_api_url = "https://korea-webtoon-api.herokuapp.com/?perPage=10000"
  #     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
  #     response = requests.get(webtoon_api_url, headers=headers)
  #     data = response.json()["webtoons"]
  #     for item in data:
  #         print(item)
  #         webtoon = Webtoon(
  #             webtoon_id= item.get('webtoonId'),
  #             title= item.get('title'),
  #             author= item.get('author'),
  #             url= item.get('url'),
  #             img= item.get('img'),
  #             service= item.get('service'),
  #             update_days= item.get('updateDays')[0],
  #             fan_count= item.get('fanCount'),
  #             search_keyword= item.get('searchKeyword'),
  #         )
  #         db.session.add(webtoon)
  #     db.session.commit()
  
  # def initialize():
  #     with app.app_context():
  #         db.create_all()
  #         if not db.session.query(Webtoon).first():  # 데이터베이스가 비어 있는지 확인
  #             create_webtoon_db()
  #             print("🚀 Webtoon DB Setiing...")
  
  if __name__ == "__main__":
      app.run(debug=True , port=5000)
      # initialize() # 서버 시작 시 초기화 작업을 수동으로 호출
      app.run(debug=True , port=5000)
  ```

- API로 받아오던 웹툰 데이터는 모두 Webtoon DB에서 받아 오는 것으로 코드를 수정했습니다.

<br/>

### 5-2. DB 데이터 변환 시 어려움
#### 문제
- db를 가져올 때 마다 딕셔너리 형태의 데이터가 아닌  문자열 배열이 출력되어 데이터를 jinja템플릿으로 보내는데 어려움이 있었습니다.

#### 문제 원인
- db를 가져올 때  `_*repr_`* 메서드의 객체 instance가 계속 출력되는 것이 문제의 원인이었습니다.
- 파이썬과 SQLite의 문법에 익숙하지 않아 필요하지 않은 메서드를 코드 상단에서 호출하고 있었기 때문에 데이터베이스가 생성될 때 원하지 않는 형식의 객체 인스턴스가 생성되었습니다.
- `__repr__` 메서드는 객체의 상태를 문자열로 변환하는 Python의 메서드로 데이터를 JSON 형식으로 출력하거나 웹 프레임워크를 사용할 때 템플릿 엔진을 활용하는 방법을 사용하여 데이터를 더 읽기 쉽고 명확한 형식으로 표시할 수 있는 메서드입니다.

#### 해결 방법
- **(방법 1) 객체를 JSON으로 변환해 사용하기**
  - Python에서 객체를 JSON 형태로 변환하려면, `json` 모듈을 사용하여 객체를 직렬화할 수 있습니다. `jsonify` 함수를 사용하여 JSON 형식으로 클라이언트에게 반환할 수 있습니다.
  - 이 방법 안 쓴 이유 : 이 리스트를 JSON 형식으로 반환하거나, 웹 페이지에서 템플릿을 통해 표시하고자 할 때, 각 `Webtoon` 객체의 속성을 적절히 처리하는데 어려움이 있어 다른 방법이 있는지 찾아 보았습니다.
- **(방법 2) `to_dict` 메서드 사용하기** **(💡 사용한 방법!)**
  - Python에서 각 객체의 속성을 수동으로 딕셔너리로 변환하거나, 모델 클래스에 `to_dict` 메서드를 추가하면 딕셔너리 형태로 변환을 자동화할 수 있습니다.
  - 저희는 SQLAlchemy 메서드인 `to_dict` 메서드를 사용하여 각 객체의 필드를 **딕셔너리 형태로 변환**하고, 변환된 딕셔너리를 **리스트**로 묶어 jinja템플릿으로 반환할 수 있었습니다.
  - 예시 코드
    ```python
    class Webtoon(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      webtoon_id = db.Column(db.Integer, nullable=False, unique=True)
      title = db.Column(db.String, nullable=False)
      author = db.Column(db.String, nullable=False)
      url = db.Column(db.String, nullable=False)
      img = db.Column(db.String, nullable=False)
      service = db.Column(db.String, nullable=False)
      update_days = db.Column(db.String, nullable=True)
      fan_count = db.Column(db.Integer, nullable=True)
      search_keyword = db.Column(db.String, nullable=False)
      
    def to_dict(self):
        return {
            "id": self.id,
            "webtoon_id": self.webtoon_id,
            "title": self.title,
            "author": self.author,
            "url": self.url,
            "img": self.img,
            "service": self.service,
            "update_days": self.update_days,
            "fan_count": self.fan_count,
            "search_keyword": self.search_keyword
        }
    
    # 데이터 조회 및 변환
    data = Webtoon.query.filter_by(service="kakao").all()
    webtoon_list = [webtoon.to_dict() for webtoon in data]
    
    # 원하는 webtoon 객체를 담은 배열로 잘 변환 되었습니다!
    print(webtoon_list)
    ```
        
<br/>
<br/>
<br/>

# 🖥️ 프로젝트 발표 장면 (@ Gather)
![](https://github.com/23thTeam/webtoon-review_project/assets/58466648/bae82604-5997-4472-913e-9bfee4a8190a)

<br/>
<br/>
<br/>

# 📝  프로젝트 회고
## 노을
### 1. KPT 회고
1. `Keep`
    - 팀 규칙을 만들고 지키는 방식이 협업하기 좋았다. 어려운 부분은 ChatGPT를 활용해야겠다.
2. `Problem`
    - 문제점
      - html에 ‘Review’ DB와 ‘Webtoon’ DB 값을 비교해서 데이터를 가져와야 하는데 ‘for in’ 반복문에 두 가지 데이터를 뿌리는 방법에 대한 어려움
    - 원인
      - 두 개의 데이터를 비교하려면 두 데이터베이스의 레코드를 연결하는 방법이 필요하다.
      - filter.by()를 사용해서 같은 ‘webtoon_id’가 있는 ‘Webtoon’DB의 값을 가져오고 싶었으나 적용하지 못했다. (새 배열을 생성해서 데이터를 넣어두고 사용했다.)
3. `Try`
    - `to_dict` 메서드 사용하기
      - 해당 메서드는 리스트 배열이기 때문에 ‘webtoon_id’를 가져오려면 인덱스를 사용해야한다.
      - 새로 알게된 메서드와 데이터 처리 방법을 사용해서 좀더 효율적인 방법으로 코드를 다시 작성!
        ```python
        filter_list = Review.query.filter_by(username=username).all()
            reviews = [review.to_dict() for review in filter_list]
        ```

### 2. 프로젝트 회고  
- 협업을 하면서 git 사용의 중요성을 알게 되었다.
- 새로운 언어나 낯선 코드를 빨리 이해할 수 있도록 연습해야겠다. 특히 협업을 할 때 다른 사람의 코드를 빠르게 읽을 수 있어야 한다는 것을 느꼈다.
- ChatGPT로 코드 작성에 도움을 처음 받아봤는데 질문의 질에 따라 좋은 답변을 해줬다. ChatGPT도 기초 지식이 있어야 유용하게 쓸 수 있는 것 같다.

<br/>

## 근우
### 1. KPT 회고
1. `Keep`
    - 협업 규칙을 세우고 규칙대로 했던 점이 좋았고 팀원별로 담당 기능이 있어서 혼자 개발하면 많았을 기능들을 각자가 맡은 부분으로 쪼개서 개발하는 부분이 좋았다.
2. `Problem`
    - 문제점
        - 개인이 개발한 API를 파이썬 애니웨어에서 사용할 수 없는 문제점
        - 데이터 변환시 어려움(DB 내에서 원하는 형태로 바로 사용할 수 없는 문제)
    - 원인
        - 파이썬 애니웨어에서는 알수없는 사용자가 해킹사이트 등에 이용하는것을 방지하기 위하여 허용된 도메인만 서버에서 에러를 발생시키지 않았다.
        - db를 가져올 때  `_*repr_`* 메서드의 객체 instance가 계속 출력되는 것이 문제의 원인이었다.
3. `Try`
    - 현실적인 방안 : 파이썬 애니웨어 유료버전을 사용할수 있으면 좋겠지만 아직 공부하는입장이라 어렵고 파이썬 애니웨어 whielist에 있는 사이트에서 API를 가져오는 방법이 있을것 같다
    - 노력 + 느낀점 : 웹 미니프로젝트라고 해서 간단할 줄 알았는데 생각보다 구현이 어렵고 시간이 오래 걸렸다.
      <br/>기술력이 많이 필요할것 같고 git을 통한 협업으로 시간을 더 효율적으로 사용해야겠다.
      <br/>git이라는 협업을 위한 체계적인 도구가 있는지 처음 알았다.

<br/>

## 은화
### 1. KPT 회고
1. `Keep` 
    - 깃허브로 협업, 어려움이 있을 때 활발히 소통한 것이 좋았습니다.
2. `Problem`
    - 문제점 : 맡은 기능을 구현하는 것을 마쳤을 때 뜨는 시간이 발생했습니다.
    - 원인 : 진행 상황에 대한 공유 부족으로 보입니다.
3. `Try`
    - 타임을 좀 더 좁게 나눠서 (예. 오전/오후/저녁) 각 타임 시작 전,  각자 진행 상황을 공유하는 시간을 가지면 좋겠습니다.

### 2. 프로젝트 전체 회고
3일간 팀원 들과 함께 미니 프로젝트를 진행하며 배운 것들을 적어보자면 다음과 같습니다.    
1. **“팀 프로젝트의 꽃, 깃허브로 협업하기”**
    - 팀원들 모두 개인적으로 깃허브 레포지토리를 사용해 본적은 있지만  깃허브로 협업을 해본 적은 없었는데, 이번 기회를 통해 각자 브런치를 생성하고 깃과 깃허브를 사용 하는 것을 배울 수 있었습니다.
    
2. **“잘 질문하고 잘 답하기 훈련, 진짜 협업의 꽃”**
    - 모르는게 있을 때, 해결해 보려고 노력해도 해결되지 않는 문제가 생길 때, 또는 팀원들에게 질문을 받을 때, 잘 질문하고 답할 수 있도록 생각을 정리하는 과정이 있었습니다.
      <br/> 팀원들, 그리고 기술 매니저님과 소통하며 문제를 하나 씩 해결해 갈때, 소통의 가치를 배웠습니다.
    
3. ”**하면 된다!”**
    - Python, Flask를 사용한 프로젝트는 처음이었지만 빨리 배울 수 있었고 프로젝트를 진행하며 재미 있었습니다.
      <br/> 맡은 기능을 구현 할 때 외부 API를 가져와 필요한 데이터를 처리하는 방법은 어려움이 없었지만 배포 환경에서의 문제로 인해 데이터를 처리하는 방식을 수정해야 하는 이슈가 발생했습니다.
      <br/> 구현할 기능이 그렇게 어렵지 않았기 때문에 나름 여유가 있었던 찰나, 이런 문제가 발생했고 새벽 4시경 까지 웹툰 DB를 생성하고 가져오는 기능을 구현하는 데 몰두하는 시간을 가졌습니다.
      <br/> 서버에 대한 지식은 별로 없었지만 기술 매니저님 과의 질문 시간과 인터넷 검색 등을 통하여 문제를 해결했을 때 큰 성취감을 느꼈습니다. 역시 하면 되긴 되는구나!
    
비록 짧은 3일간의 기간이었지만 팀원들과 정도 많이 든것 같네요.
<br/>늘 열심인 노을님, 근우님! 팀 프로젝트는 여기서 끝이지만 우리 모두 이노캠 끝까지 잘 달려 봅시다! 화이팅! 🔥
<br/>

### 3. 프로젝트 아쉬웠던 점 회고
그리고 개인적으로 프로젝트를 마무리하며 아쉬웠던 점 두 가지가 있습니다.
1. REST Full API 설계 방식을 따르지 못한 부분이 아쉽습니다. 리뷰 데이터를 CRUD 하는 과정과 웹툰을 서치하는 과정에서 엔드 포인트 수정이 필요해 보입니다.
2. DB를 설계할 때, Webtoon 데이터에 Review 데이터를 1대N 관계로 매핑하지 못한 점이 아쉽습니다.
