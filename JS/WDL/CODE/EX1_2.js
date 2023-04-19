// A가 짝수인지 홀수인지 0인지 알려주는 프로그램

let A = 10;

switch (A % 2){
  case 0:
    console.log('짝수');
    break;
  case 1:
    console.log('홀수');
    break;
}

// 연산자
A % 2 === 0 ? console.log('짝수') : console.log('홀수');