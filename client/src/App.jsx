// client/src/App.jsx
import React, { useState, useEffect } from 'react';

function App() {
  const [aboutMessage, setAboutMessage] = useState('');

  // useEffect(() => {
  //   fetch('/api/about') // Relative path to your API route
  //     .then(response => response.json())
  //     .then(data => setAboutMessage(data.message))
  //     .catch(error => console.error('Error fetching about page:', error));
  // }, []);

  return (
    <div>
      <h1>About</h1>
      <p>{aboutMessage}</p>
    </div>
  );
}

export default App;
