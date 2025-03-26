<h1 align="center">System Resource Test Scripts</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Platform-AWS-brightgreen.svg" alt="Platform">
</p>

<p>
A collection of Python scripts for testing system resource consumption and performance monitoring.
</p>

<hr>

<h2>📜 Scripts</h2>

<h3>1. Memory Consumption Test (<code>INC_MEMORY.py</code>)</h3>

<p>Tests system behavior under increasing memory load.</p>

<h4>Features</h4>
<ul>
<li> Allocates memory in 100MB chunks</li>
<li> Displays real-time memory allocation</li>
<li> Can be stopped with Ctrl+C</li>
<li> Includes 1-second delay between allocations</li>
</ul>

<h4>Usage</h4>

```bash
python3 INC_MEMORY.py
```


<h3>2. CPU Load Simulator (<code>INC_CPU_LOAD.py</code>)</h3>

<p>Simulates increasing CPU load by running multiple CPU-intensive tasks.</p>

<h4>Features</h4>
<ul>
<li> Creates CPU load by calculating prime numbers</li>
<li> Incrementally spawns multiple threads</li>
<li> Configurable increase rate and duration</li>
<li> Shows number of running tasks</li>
</ul>

<h4>Usage</h4>

```bash
python INC_CPU_LOAD.py
```

<strong>Parameters:</strong>
- `increase_rate`: Number of new tasks to add per second
- `duration`: How long to increase load (in seconds)

<strong>Example:</strong>
```python
simulate_cpu_load(increase_rate=2, duration=10)  # Adds 2 tasks/second for 10 seconds
```

<h2>⚠️ Warning</h2>

<p>
Use these scripts with caution:</p>
<ul>
<li> The memory script will consume system memory until stopped</li>
<li> The CPU script can cause high processor utilization</li>
<li> May impact system stability if resources are exhausted</li>
</ul>

<h2>📋 Requirements</h2>

<ul>

<li> Python 3.x</li>
<li> No additional dependencies required</li>
</ul>

<hr>

<p align="center">
Made for system testing and monitoring
</p>