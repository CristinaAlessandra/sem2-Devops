from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()

    assert result == {"teste":True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_test = Estudante(name="João", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_test)
    assert estudante_test == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10)
    assert result

# Testes adicionados posteriormente by Alessandra
@pytest.mark.asyncio
async def test_activate_estudante():
    result = await activate_estudante(True)
    assert result

@pytest.mark.asyncio
async def test_deactivate_estudante():
    result = await deactivate_estudante(True)
    assert result

@pytest.mark.asyncio
async def test_getByName_estudante():
    nome_test = "João"
    result = await getByName_estudante(nome_test)
    assert nome_test == result

@pytest.mark.asyncio
async def test_getAll():
    result = await getAll()
    assert isinstance(result, list)
    assert {"name": "Maria", "curso": "Análise e Desenvolvimento de Sistemas", "ativo": True} in result

@pytest.mark.asyncio
async def test_getCursos():
    result = await getCursos()
    assert isinstance(result, dict)
    assert "cursos" in result
    assert "Sistemas de Informação" in result["cursos"]
