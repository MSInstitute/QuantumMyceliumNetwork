# src/tests/test_network.py

import pytest
import numpy as np
from quantum_mycelium.network import QuantumMyceliumNetwork
from quantum_mycelium.quantum.state_manager import QuantumStateManager

@pytest.fixture
def network():
    """Create a test network instance."""
    return QuantumMyceliumNetwork(
        dimensions=3,
        initial_nodes=10,
        quantum_enabled=True
    )

def test_network_initialization(network):
    """Test network initialization."""
    assert network.dimensions == 3
    assert len(network.nodes) == 10
    assert hasattr(network, 'quantum_manager')

def test_quantum_state_creation(network):
    """Test quantum state creation."""
    state = network.quantum_manager.create_quantum_state()
    assert isinstance(state, np.ndarray)
    assert len(state) == 2
    assert np.allclose(np.sum(np.abs(state)**2), 1)

def test_signal_propagation(network):
    """Test signal propagation through network."""
    test_data = b"Test research data"
    origin_node = list(network.nodes.keys())[0]
    
    propagation_time = network.propagate_signal(
        data=test_data,
        origin_node=origin_node
    )
    
    assert isinstance(propagation_time, float)
    assert propagation_time > 0

def test_network_adaptation(network):
    """Test network topology adaptation."""
    initial_nodes = len(network.nodes)
    network.adapt_topology()
    assert len(network.nodes) >= initial_nodes

def test_research_validation(network):
    """Test research validation process."""
    test_research = b"Sample research data for validation"
    
    result = network.validate_research(
        research_data=test_research,
        confidence_threshold=0.95
    )
    
    assert isinstance(result, dict)
    assert 'validated' in result
    assert 'confidence' in result
    assert 'time_taken' in result
    assert result['confidence'] > 0

def test_quantum_entanglement(network):
    """Test quantum entanglement between nodes."""
    nodes = list(network.nodes.keys())[:2]
    entangled_pairs = network.quantum_manager.entangle_nodes(
        {node: network.nodes[node] for node in nodes}
    )
    
    assert isinstance(entangled_pairs, dict)
    assert len(entangled_pairs) > 0

def test_error_handling(network):
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        network.propagate_signal(
            data=b"Test data",
            origin_node="nonexistent_node"
        )

def test_network_scaling(network):
    """Test network scaling capabilities."""
    initial_size = len(network.nodes)
    
    # Simulate high load
    for _ in range(5):
        network.adapt_topology()
    
    final_size = len(network.nodes)
    assert final_size > initial_size
    
def test_validation_consensus(network):
    """Test consensus achievement in validation."""
    test_data = b"Consensus test data"
    
    # Perform multiple validations
    results = []
    for _ in range(5):
        result = network.validate_research(test_data)
        results.append(result['validated'])
    
    # Check consensus stability
    assert len(set(results)) == 1  # All results should be consistent

def test_quantum_signature(network):
    """Test quantum signature creation and verification."""
    test_data = b"Test data for signing"
    
    # Create signature
    signature = network.quantum_manager.create_signature(test_data)
    
    # Verify signature
    is_valid = network.quantum_manager.verify_signature(test_data, signature)
    assert is_valid