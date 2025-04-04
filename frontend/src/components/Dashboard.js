import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

function Dashboard() {
  const [traffic, setTraffic] = useState({ 
    north: 0, south: 0, east: 0, west: 0, emergency: false 
  });

  useEffect(() => {
    socket.on('traffic_update', (data) => {
      setTraffic(data);
    });
  }, []);

  return (
    <div>
      <h1>Smart Traffic Management</h1>
      <div className="traffic-lights">
        <div className="lane" style={{ backgroundColor: traffic.north > 10 ? 'red' : 'green' }}>
          North: {traffic.north}
        </div>
        <div className="lane" style={{ backgroundColor: traffic.south > 10 ? 'red' : 'green' }}>
          South: {traffic.south}
        </div>
        <div className="lane" style={{ backgroundColor: traffic.east > 10 ? 'red' : 'green' }}>
          East: {traffic.east}
        </div>
        <div className="lane" style={{ backgroundColor: traffic.west > 10 ? 'red' : 'green' }}>
          West: {traffic.west}
        </div>
      </div>
      {traffic.emergency && <div className="emergency-alert">🚑 Emergency Vehicle Detected!</div>}
    </div>
  );
}

export default Dashboard;
