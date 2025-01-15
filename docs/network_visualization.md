# Network Visualization

![Network Visualization Example](../assets/network_preview.svg)

## Interactive Network View

Our quantum mycelial network provides real-time visualization of:
- Hyphal connections
- Quantum state transfers
- Validation processes
- Network growth patterns

## Visualization Types

### 1. Network Topology
```python
from quantum_mycelium.viz import NetworkVisualizer

viz = NetworkVisualizer(network)
viz.plot_topology(
    show_quantum_states=True,
    highlight_active=True
)
```

### 2. Growth Patterns
```python
viz.plot_growth_patterns(
    time_window=3600,  # 1 hour
    show_connections=True
)
```

### 3. Validation Flow
```python
viz.plot_validation_flow(
    node_ids=['node_1', 'node_2'],
    show_quantum_states=True
)
```

## Customization Options

### Color Schemes
- Hyphal Hub: White (#FFFFFF)
- Spore Transfer: Light Blue (#88CCFF)
- Validator: Green (#44FF88)
- Quantum Node: Pink (#FF88AA)

### Layout Settings
- Force Atlas 2 algorithm
- Gravity: 0.5
- Scaling: 50.0
- Edge bundling enabled

## Integration with Tools

### Gephi Export
```python
viz.export_to_gephi(
    filename='mycelial_network.gephi',
    include_quantum_states=True
)
```

### D3.js Web Visualization
```python
viz.export_to_d3(
    output='web/network.json',
    interactive=True
)
```

## Example Visualizations

1. Real-time Network Growth
2. Quantum State Propagation
3. Validation Consensus Building
4. Resource Distribution Flow

## Usage Guide

### Basic Setup
```python
# Initialize visualizer
viz = NetworkVisualizer(network)

# Create basic visualization
viz.plot_network()

# Enable real-time updates
viz.start_live_updates(
    interval=1.0,
    save_snapshots=True
)
```

### Advanced Features
```python
# 3D visualization
viz.plot_3d(
    rotate=True,
    highlight_quantum=True
)

# Animation
viz.create_animation(
    duration=10,
    fps=30,
    output='network_growth.gif'
)
```
