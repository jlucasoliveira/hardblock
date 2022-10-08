from core.managers import BaseManager


class CounterManager(BaseManager):
    def create_shared_counter(self, unit_id: str):
        counter = self.model(
            name="Sala de espera de exames",
            description="Sala onde os pacientes são chamados para a realização de exames",
            unit_id=unit_id,
            attendance_amount=15,
            shared=True,
        )
        counter.save(using=self._db)
        return counter
