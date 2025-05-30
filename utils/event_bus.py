class EventBus:
    _subscribers = {}

    @classmethod
    def subscribe(cls, event_type, handler):
        if event_type not in cls._subscribers:
            cls._subscribers[event_type] = []
        cls._subscribers[event_type].append(handler)

    @classmethod
    def publish(cls, event_type, data):
        if event_type in cls._subscribers:
            for handler in cls._subscribers[event_type]:
                handler(data)
