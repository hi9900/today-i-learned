> [TS Playgound](https://www.typescriptlang.org/play)
>
> 자동으로 TypeScript 코드를 JavaScript 코드로 변환하고, 변환된 코드를 보여준다.

### TypeScript 설치

- Node.js 설치 후 TypeScript 설치

```bash
$ npm install typescript --save-dev
```

### 프로젝트 초기화

- TypeScript 프로젝트를 초기화하려면 다음 명령어를 실행한다.

  이 명령어는 `tsconfig.json` 파일을 생성한다.

```bash
$ npx tsc --init
```

- `tsconfig.json` 파일을 열고 다음 설정을 추가한다.

  이 설정은 "src" 폴더에 있는 모든 TypeScript 파일을 컴파일하고, 결과를 "build" 폴더에 저장한다.

```json
{
  "include": ["src"],
  "compilerOptions": {
    "outDir": "./build"
  }
}
```

### TypeScript 컴파일

- TypeScript 컴파일러를 사용하려면

```bash
$ npx tsc
```

- TypeScript 파일의 변경사항을 실시간으로 감지하고 컴파일하려면

```bash
$ npx tsc --watch
```

### TypeScript 추가 공부 주제

- 인터페이스

- 제네릭

- 네임스페이스와 모듈

- 타입 가드와 타입 단언

- 맵드 타입과 조건부 타입

- 유틸리티 타입

- 타입스크립트와 함께 사용되는 라이브러리 및 프레임워크
