# Design

## Data Entities

### 名詞・名詞句

- チケット料金
- ユーザー
    - シネマシティズン
    - シネマシティズン（60才以上）
    - 一般
    - シニア（70才以上）
    - 学生（大・専）
    - 中・高校生
    - 幼児（3才以上）・小学生
    - 障がい者（学生以上）
    - 障がい者（高校以下）
- 上映日時
    - 平日
    - 土日祝
    - 映画の日（毎月1日）
    - 20時まで
    - レイトショー

### モデリング

- チケット料金(ticket_price)
    - シネマシティズン(member)
    - シニアシネマシティズン (senior_member)
    - 一般 (general)
    - シニア (senior)
    - 学生 (student)
    - 中・高校生 (middle_or_high_school_student)
    - 幼児・小学生 (elementary_school_or_younger_student)
    - 障がい者一般 (general_with_disability)
    - 障がい者高校以下 (younger_with_disability)
- 上映日時(screening_datetime)
    - 平日(weekday)
    - 土日祝(holiday)
    - 映画の日(movie_day)
    - レイトショー(late_show)
- ユーザー(user)
    - 年齢(age)
    - 学生フラグ(is_student)
    - 中高生フラグ(is_middle_or_high_school)
    - 小学生以下フラグ(is_elementary_school_or_younger)
    - 障害者フラグ(has_disability)
    - 会員フラグ(is_member)

## Functions

- チケット料金
    - 計算する(calculate)
- 上映日時
    - 土日祝か判定する(is_holiday)
    - 映画の日か判定する(is_movie_day)
    - レイトショーか判定する(is_late_show)
- ユーザー
    - 会員の年齢割引対象か判定する(is_member_age_discount)
    - シニアか判定する(is_senior)
