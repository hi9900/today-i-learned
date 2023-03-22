// for 문으로 구구단 프로그램 만들기

// 2단

let A = 2;

for (let i = 1; i < 10; i++){
  // console.log(A,'*', i, '=', A * i);
}

// 2단 ~ 9단

for (let i = 2; i < 10; i ++){
  for (let j = 1; j < 10; j++){
    console.log(i, '*', j, '=', i*j);
  }
}