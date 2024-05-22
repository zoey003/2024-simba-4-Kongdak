# 2024-simba-4-Kongdak

심바톤 4팀 콩닥콩닥 팀 리포지토리입니다 🥰

| ![zoey003](https://github.com/zoey003.png) | ![sayyyho](https://github.com/sayyyho.png) | ![chaem03](https://github.com/chaem03.png) | ![pyeree](https://github.com/pyeree.png) | ![onlynyang](https://github.com/onlynyang.png) |
| :----------------------------------------: | :----------------------------------------: | :----------------------------------------: | :--------------------------------------: | :--------------------------------------------: |
|    [김지현](https://github.com/zoey003)    |    [박세호](https://github.com/sayyyho)    |    [하채민](https://github.com/chaem03)    |   [임현우](https://github.com/pyeree)    |     [한지은](https://github.com/onlynyang)     |
|                     PD                     |                     FE                     |                     FE                     |                    BE                    |                       BE                       |
|                  경제학과                  |               정보통신공학과               |               전자전기공학부               |              정보통신공학과              |                    통계학과                    |
|               기획 및 디자인               |                 UI/UX 구현                 |                 UI/UX 구현                 |       DB 구축 및 API 구현 및 배포        |          DB 구축 및 API 구현 및 배포           |

# GitHub Role

해당 Repository는 다음과 같은 규칙을 따르고 있습니다.

## GitHub Branch

### Flow Strategy

- 사용자는 먼저 Upstream Repository를 자신의 GitHub 계정으로 포크(fork)하고, 이 포크(fork)된 Origin Repository를 로컬 컴퓨터로 **Clone**하여 작업합니다.

- 그 후 개발한 변경 사항을 Origin Repository로 **Push**합니다. 이후 Upstream Repository로 풀 **PR**를 보내 변경 사항을 제안합니다.

- PR이 완료 된 후 Upstream Repository의 최신 변경 사항을 가져오기 위해 Local에서 풀(pull)을 사용합니다.

### 개발을 시작할 때

1. 개발을 시작할 때는 Upstream Repository에서 Issue를 생성합니다.
2. 이후 Issue에서 Origin Repository의 Dev Branch에서 새로운 Branch를 생성합니다
   - 이때 브랜치 이름은 다음을 따릅니다.
   - **새로운 기능 개발 : feature/#[Issue의 번호]**
   - **버그 픽스 : fix/#[Issue의 번호]**
   - **기능 리팩토링 : refactor/#[Issue의 번호]**
3. Loacl에서 Fetch를 통해 만든 New Branch(feature or fix or refactor)을 들고옵니다.
4. 해당 Branch로 checkout 이후 기능 개발을 진행합니다.

### 개발을 종료할 때

1. 기능 개발이 종료되면 Origin Repository의 Branch(feature or fix or refactor)로 변경 사항을 Push 합니다.
2. Origin Repository에서 Upstream Repository로 PR을 보냅니다.
3. Code Review 이후 마지막으로 Approve한 사람은 **_Squash And Merge_**를 합니다.
4. PR이 **_Squash And Merge_**되면 Local에서는 dev Branch로 checkout합니다.
5. Local에서 Upstream Repository의 dev Branch를 pull 받습니다.
6. 마지막으로 Origin Repository의 dev Branch를 Update하기 위해 Push를 해줍니다.

### Main Branch가 갱신될 때

1. 만약 Release Version을 낼 때는 Upstream의 dev Branch에서 main Branch로 PR을 날립니다.
2. 해당 Repository의 모든 사용자가 Code를 재확인한 후 Merge를 합니다.

## Branch Naming Convention

| Commit Type | Description           |
| ----------- | --------------------- |
| Main        | 테스트 완료 후 배포용 |
| Test        | A/B 테스트용          |
| QA          | QA용                  |
| Dev         | 개발 커밋 통합용      |
| Feat        | 기능 개발용           |
| Fix         | 버그 수정용           |
| Refactor    | 코드 리팩토링         |

## Commit Convention

| Commit Type | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| Feat        | 기능 개발                                                      |
| Fix         | 버그 수정                                                      |
| Docs        | 문서 수정                                                      |
| Style       | 코드 formatting, 세미콜론 누락 등 코드 자체의 변경이 없는 경우 |
| Refactor    | 코드 리팩토링                                                  |
| Chore       | package manager 수정 등                                        |
| Design      | CSS 등 사용자 UI 변경                                          |

## PR Convention

| Icon | 사용법       | Description              |
| ---- | ------------ | ------------------------ |
| 🎨   | `:art`       | 코드 구조/서식 개선      |
| ⚡️  | `:zap`       | 성능 향상                |
| 🔥   | `:fire`      | 코드/파일 삭제           |
| 🐛   | `:bug`       | 버그 수정                |
| 🚑   | `:ambulance` | 긴급 수정                |
| ✨   | `:sparkles`  | 새로운 기능 도입         |
| 💄   | `:lipstick`  | UI/스타일 파일 추가/수정 |
