from abc import ABC, abstractmethod
from kura.types.cluster import Cluster


class BaseMetaClusterModel(ABC):
    @abstractmethod
    def reduce_clusters(self, clusters: list[Cluster]) -> list[Cluster]:
        pass