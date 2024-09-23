from myproj.service.service import ServiceRepo
import pytest


def test_get_services(service_repo_from_list):
    services = service_repo_from_list.get_services()
    assert len(services) == 2


def test_find_by_id(service_repo_from_list):
    s1 = service_repo_from_list.find_by_id(1)
    assert s1.id_ == 1


def test_find_by_id_not_found(service_repo_from_list):
    with pytest.raises(KeyError) as e:
        s = service_repo_from_list.find_by_id(111)
    assert str(e.value) == "'Service Not Found'"


def test_update(service_repo_from_list):
    updated_service = service_repo_from_list.update(1, {"name": "UpdatedService"})
    assert updated_service.name == "UpdatedService"
    assert service_repo_from_list.find_by_id(1).name == "UpdatedService"


def test_not_update(service_repo_from_list):
    with pytest.raises(KeyError) as e:
        updated_service = service_repo_from_list.update(222, {"name": "UpdatedService"})
    assert str(e.value) == "'Service Not Found'"


def test_delete(service_repo_from_list):
    service_repo_from_list.delete(1)
    assert len(service_repo_from_list.get_services()) == 1
    with pytest.raises(KeyError) as e:
        service_repo_from_list.find_by_id(1)
    assert str(e.value) == "'Service Not Found'"


def test_delete_not_found(service_repo_from_list):
    with pytest.raises(KeyError) as e:
        service_repo_from_list.delete(2222)
    assert str(e.value) == "'Service Not Found'"
