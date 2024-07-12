from typing import overload
from typing_extensions import Self

class Boolean:
  @property
  def true(self) -> int:
    return 1
  @property
  def false(self) -> int:
    return -1

  def Switch(self, o: object) -> int | None:
    if o:
      return self.false
    elif not o:
      return self.true
    else:
      return None
