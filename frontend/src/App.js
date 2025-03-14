import React, { useState } from 'react';

function App() {
  const [result, setResult] = useState('');
  const [logData, setLogData] = useState('');
  const [timestamp, setTimestamp] = useState('');

  const handleSubmit = async () => {
    const response = await fetch('http://localhost:8000/process-logs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ log_data: logData, timestamp: timestamp })
    });

    const data = await response.json();
    setResult(data.result || data.detail);
  };

  return (
    <div>
      <h1>Root Cause Analysis</h1>
      <input 
        type="text" 
        placeholder="Log Data" 
        value={logData} 
        onChange={(e) => setLogData(e.target.value)} 
      />
      <input 
        type="datetime-local" 
        value={timestamp} 
        onChange={(e) => setTimestamp(e.target.value)} 
      />
      <button onClick={handleSubmit}>Submit</button>
      <p>Result: {result}</p>
    </div>
  );
}

export default App;
