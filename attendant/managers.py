from core import managers


class PriorityManager(managers.BaseManager):
    def create_general_priority(self, unit):
        priority = self.model(
            name="Normal",
            description="Prioridade comum",
            abbreviation="N",
            personalized_service=True,
            importance=0.3,
        )
        priority.save(using=self._db)
        unit.priority_set.add(priority)
        return priority

