# API Reference

## Core Components

### QuantumMyceliumNetwork

The main class for network operations and validation.

```python
from quantum_mycelium.core.network import QuantumMyceliumNetwork

network = QuantumMyceliumNetwork(
    dimensions=3,
    initial_nodes=1000,
    quantum_enabled=True
)
```

#### Key Methods

- `propagate_signal(data: bytes, origin_node: str) -> float`
  - Propagates quantum-encoded data through the network
  - Returns propagation time in femtoseconds

- `validate_research(research_data: bytes, confidence_threshold: float = 0.95) -> Dict`
  - Validates research using quantum mycelial consensus
  - Returns validation results including confidence scores

- `adapt_topology() -> None`
  - Adapts network topology based on usage patterns

### QuantumStateManager

Manages quantum states and entanglement operations.

```python
from quantum_mycelium.quantum.state_manager import QuantumStateManager

manager = QuantumStateManager(coherence_time=1000)
```

#### Key Methods

- `create_quantum_state() -> np.ndarray`
- `entangle_nodes(nodes: Dict) -> Dict[str, List[str]]`
- `measure_coherence() -> float`

### MycelialGrowthPattern

Implements biological growth patterns for network adaptation.

```python
from quantum_mycelium.bio.growth_patterns import MycelialGrowthPattern

pattern = MycelialGrowthPattern(
    quantum_manager=manager,
    params=GrowthParameters()
)
```

## Usage Examples

### Basic Validation

```python
# Initialize network
network = QuantumMyceliumNetwork()

# Validate research
result = network.validate_research(
    research_data=b"Sample research data"
)

print(f"Validation result: {result['validated']}")
print(f"Confidence: {result['confidence']}")
```

### Advanced Network Operations

```python
# Adapt network topology
network.adapt_topology()

# Propagate quantum signals
propagation_time = network.propagate_signal(
    data=b"Critical data",
    origin_node="node_0"
)
```

## Error Handling

```python
try:
    result = network.validate_research(research_data)
except QuantumDecoherenceError:
    print("Quantum state lost coherence")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

## Configuration

```python
# Network configuration
config = {
    "quantum": {
        "coherence_time": 1000,
        "entanglement_type": "spore-based"
    },
    "network": {
        "growth_factor": 1.618,
        "min_nodes": 100
    }
}

network = QuantumMyceliumNetwork(**config)
```
