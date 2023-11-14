##  import
Было:
```python
<пусто>
```
Стало:
```python
import datetime
```
***

##  def get_age(self) -> int:
Было:
```python
now: datetime.datetime = datetime.datetime.now()
return self.yob - now.year
```
Стало:
```python
now: datetime.datetime = datetime.datetime.now()
return now.year - self.yob
```
***

##  def set_name(self, name: str) -> None:
Было:
```python
self.name = self.name
```
Стало:
```python
self.name = name
```
***

##  def set_address(self, address: str) -> None:
Было:
```python
self.address == address
```
Стало:
```python
self.address = address
```
***

##  def is_homeless(self) -> bool:
Было:
```python
return address is None
```
Стало:
```python
return True if not self.get_address() else False
```
***
