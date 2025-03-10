## Classes

```ts
class Player {
  constructor(
    private firstName: string,
    private lastName: string,
    public nickname: string
  ) {}
}
const hi = new Player("hi", "ㅎ", "ㅇ");

hi.nickname;
```

## 추상 클래스

- 다른 클래스가 상속받을 수 있는 클래스

- 새로운 인스턴스를 만들 수 없다.

  오직 다른 곳에서 상속만 받을 수 있음

```ts
abstract class User {
  constructor(
    private firstName: string,
    private lastName: string,
    public nickname: string
  ) {}
}

class Player extends User {}
const hi = new Player("hi", "ㅎ", "ㅇ");

hi.nickname;
```

### 추상 메소드 (abstract method)

- private 및 public은 property 뿐 아니라 method에서도 작동함

```ts
abstract class User {
  constructor(
    private firstName: string,
    private lastName: string,
    public nickname: string
  ) {}
  // private로 만들면 더 이상 작동하지 않음
  // private getFullName () {
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
}

class Player extends User {}
const hi = new Player("hi", "ㅎ", "ㅇ");

hi.getFullName();
```

- 추상 메소드: 추상 클래스를 상속받는 모든 것들이 구현을 해야하는 메소드

- property를 private로 만들면, 그 클래스를 상속하였더라도 property에 접근할 수 없음

- protected: 클래스 밖에서는 접근할 수 없지만, 상속 받은 클래스에서는 사용할 수 있음

```ts
abstract class User {
  constructor(
    protected firstName: string,
    protected lastName: string,
    protected nickname: string
  ) {}

  abstract getNickName(): void;
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }
}

class Player extends User {
  getNickName() {
    console.log(this.nickname);
  }
}
const hi = new Player("hi", "ㅎ", "ㅇ");
hi.getFullName();
hi.firstName();
```
