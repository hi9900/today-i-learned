# Many To Many Relationship

> ### [참고] 데이터 모델링

  - 주어진 개넘으로부터 논리적인 데이터 모델을 구성하는 작업

  - 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업

### target model

  관계 필드를 가지지 않은 모델

### source model

  관계 필드를 가진 모델

---

- 병원에 내원하는 환자와 의사의 예약 시스템을 구축

## N:1의 한계

- 의사와 환자 간 예약 시스템을 구현

- 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정 (N:1)

- 동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어 예약을 진행해야 함

  새로운 환자 객체를 생성해야 함

- 외래 키 컬럼에 '1, 2' 형태로 참조하는 것은 Integer 타입이 아니기 때문에 불가능

- 예약 테이블을 따로 만들기

## 중개모델

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성

- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

```python
# hospitals/models.py

class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

- 의사와 환자 생성 후 예약 만들기

```shell
doctor1 = Doctor.objects.create(name='doctor1')
patient1 = Patient.object.create(name='patient1')

Reservation.object.create(doctor=doctor1, patient=patient1)
```

- 예약 정보 조회

```shell
# 의사 -> 예약 정보 찾기
doctor1.reservation_set.all()

# 환자 -> 예약 정보 찾기
patient1.reservation_set.all()
```

## Django ManyToManyField

- Django는 `ManyToManyField`를 통해 중개 테이블을 자동으로 생성한다.

- 환자 모델에 Django `ManyToManyField` 작성

```python
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor)
  name = models.TextField()
```

- 데이터베이스 초기화, Migration 진행 후 생성된 중개 테이블 `hospitals_patient_doctors` 확인

- 예약 생성

```shell
# 의사 1명과 환자 2명 생성
doctor1 = Doctor.objects.create(name='doct1')
patient1 = Patient.objects.create(name='pat1')
patient2 = Patient.objects.create(name='pat2')

# 예약: 환자가 의사에게 예약
patient1.doctors.add(doctor1)
# 예약: 의사가 환자를 예약
doctor1.patient_set.add(patient2)

# doctor1의 예약 환자 목록 확인
doctor1.patient_set.all()
# patient이 예약한 의사 목록 확인
patient1.doctors.all()
patient2.doctors.all()

# 예약 취소(삭제)
# doctor1의 patient1 예약 취소
doctor1.patient_set.remove(patient1)
```

> ### 'related_name' argument

- target model이 source model을 참조할 때 사용햘 manager name

- ForeignKey()의 related_name과 동일

> ### 'through' argument

- 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음

- 가장 일반적인 용도는 중개 테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우

- through 설정 및 Reservation Class 수정

  예약 정보에 증상과 예약일이라는 추가 데이터 생성

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(autu_now_add=True)
```

```shell
# 의사 1명과 환자 2명 생성
doctor1 = Doctor.objects.create(name='doct1')
patient1 = Patient.objects.create(name='pat1')
patient2 = Patient.objects.create(name='pat2')

# 예약 생성 1. Reservation class를 통한 예약 생성
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()

# 예약 생성 2. Patient 객체를 통한 예약 생성
# through_defaults 값에 딕셔너리 타입으로 입력
patient2.doctors.add(doctor1, through_defaults={'symptom':'flu'})
```

## 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음

- Django의 ManyToManyField는 중개 테이블을 자동으로 생성함

- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음

  대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

- N:1은 완전한 종속의 관계였지만, M:N은 두 가지 형태로 모두 표현이 가능함.