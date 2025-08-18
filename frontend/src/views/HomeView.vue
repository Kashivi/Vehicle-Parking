<template>
  <div class="home">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Main Content -->
    <div class="content-wrapper">
      <!-- Header Section -->
      <div class="header-section">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
          </svg>
        </div>
        
        <h1 class="main-title">
          <span class="gradient-text">ParkSmart</span>
        </h1>
        <p class="subtitle">Intelligent Vehicle Parking Management System</p>
        <p class="description">
          Streamline your parking operations with real-time monitoring, 
          automated billing, and smart space allocation.
        </p>
      </div>

      <!-- Features Grid -->
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🚗</div>
          <h3>Smart Allocation</h3>
          <p>AI-powered space optimization</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📱</div>
          <h3>Mobile Access</h3>
          <p>Manage parking on the go</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">💳</div>
          <h3>Digital Payments</h3>
          <p>Seamless transaction processing</p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="action-section">
        <router-link to="/login" class="btn btn-primary">
          <span class="btn-content">
            <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/>
              <polyline points="10,17 15,12 10,7"/>
              <line x1="15" y1="12" x2="3" y2="12"/>
            </svg>
            Login
          </span>
        </router-link>
        
        <router-link to="/register" class="btn btn-secondary">
          <span class="btn-content">
            <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="8.5" cy="7" r="4"/>
              <line x1="20" y1="8" x2="20" y2="14"/>
              <line x1="23" y1="11" x2="17" y2="11"/>
            </svg>
            Register
          </span>
        </router-link>
      </div>

      <!-- Stats Section -->
      <div class="stats-section">
        <div class="stat-item">
          <div class="stat-number">99.9%</div>
          <div class="stat-label">Uptime</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">1000+</div>
          <div class="stat-label">Parking Spots</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">24/7</div>
          <div class="stat-label">Support</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped>
/* Color Variables - Parking Theme */
:root {
  --primary-blue: #1e40af;      /* Deep parking sign blue */
  --secondary-blue: #3b82f6;    /* Lighter blue */
  --accent-orange: #f59e0b;     /* Warning/caution orange */
  --success-green: #10b981;     /* Available space green */
  --dark-gray: #1f2937;         /* Asphalt dark */
  --medium-gray: #6b7280;       /* Road gray */
  --light-gray: #f3f4f6;        /* Concrete light */
  --white: #ffffff;
  --shadow: rgba(0, 0, 0, 0.1);
  --shadow-dark: rgba(0, 0, 0, 0.2);
}

.home {
  min-height: 100vh;
  background: linear-gradient(135deg, var(--dark-gray) 0%, var(--medium-gray) 50%, var(--light-gray) 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

/* Animated Background Pattern */
.bg-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 48px,
      rgba(255, 255, 255, 0.03) 50px,
      rgba(255, 255, 255, 0.03) 52px
    ),
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 48px,
      rgba(255, 255, 255, 0.03) 50px,
      rgba(255, 255, 255, 0.03) 52px
    );
  animation: drift 20s linear infinite;
}

@keyframes drift {
  0% { transform: translate(0, 0); }
  100% { transform: translate(50px, 50px); }
}

.content-wrapper {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 60px 40px;
  max-width: 800px;
  width: 100%;
  box-shadow: 
    0 20px 60px var(--shadow-dark),
    0 0 0 1px rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  position: relative;
  z-index: 1;
}

/* Header Section */
.header-section {
  text-align: center;
  margin-bottom: 50px;
}

.parking-icon {
  display: inline-block;
  margin-bottom: 20px;
  color: var(--primary-blue);
  animation: float 3s ease-in-out infinite;
}

.parking-icon .icon {
  width: 80px;
  height: 80px;
  filter: drop-shadow(0 4px 12px var(--shadow));
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

.main-title {
  font-size: 3.5em;
  font-weight: 800;
  margin-bottom: 10px;
  letter-spacing: -2px;
}

.gradient-text {
  background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue), var(--accent-orange));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.subtitle {
  font-size: 1.3em;
  color: var(--medium-gray);
  font-weight: 600;
  margin-bottom: 15px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.description {
  font-size: 1.1em;
  color: var(--medium-gray);
  line-height: 1.6;
  max-width: 600px;
  margin: 0 auto;
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 50px;
}

.feature-card {
  background: linear-gradient(145deg, var(--white), var(--light-gray));
  padding: 30px 20px;
  border-radius: 16px;
  text-align: center;
  box-shadow: 
    0 8px 32px var(--shadow),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
  transition: left 0.5s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 
    0 12px 48px var(--shadow-dark),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
}

.feature-card:hover::before {
  left: 100%;
}

.feature-icon {
  font-size: 2.5em;
  margin-bottom: 15px;
  display: block;
}

.feature-card h3 {
  font-size: 1.2em;
  font-weight: 700;
  color: var(--dark-gray);
  margin-bottom: 8px;
}

.feature-card p {
  color: var(--medium-gray);
  font-size: 0.95em;
}

/* Action Buttons */
.action-section {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 50px;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 16px 32px;
  font-size: 1.1em;
  font-weight: 600;
  text-decoration: none;
  border-radius: 12px;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  min-width: 160px;
  position: relative;
  overflow: hidden;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-content {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 20px;
  height: 20px;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
  color: var(--white);
  box-shadow: 0 8px 32px rgba(30, 64, 175, 0.3);
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, var(--secondary-blue), var(--accent-orange));
  transition: left 0.3s ease;
  z-index: 1;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 48px rgba(30, 64, 175, 0.4);
}

.btn-primary:hover::before {
  left: 0;
}

.btn-secondary {
  background: var(--white);
  color: var(--primary-blue);
  border: 2px solid var(--primary-blue);
  box-shadow: 0 8px 32px var(--shadow);
}

.btn-secondary:hover {
  background: var(--primary-blue);
  color: var(--white);
  transform: translateY(-2px);
  box-shadow: 0 12px 48px rgba(30, 64, 175, 0.3);
}

/* Stats Section */
.stats-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 30px;
  padding-top: 40px;
  border-top: 2px solid var(--light-gray);
}

.stat-item {
  text-align: center;
  padding: 20px;
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.8), rgba(243, 244, 246, 0.8));
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(5px);
  transition: transform 0.3s ease;
}

.stat-item:hover {
  transform: scale(1.05);
}

.stat-number {
  font-size: 2.2em;
  font-weight: 800;
  color: var(--primary-blue);
  margin-bottom: 5px;
  text-shadow: 0 2px 4px var(--shadow);
}

.stat-label {
  font-size: 0.9em;
  color: var(--medium-gray);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .content-wrapper {
    padding: 40px 20px;
    margin: 10px;
  }
  
  .main-title {
    font-size: 2.5em;
  }
  
  .action-section {
    flex-direction: column;
    align-items: center;
  }
  
  .btn {
    width: 100%;
    max-width: 280px;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .stats-section {
    grid-template-columns: 1fr;
    gap: 15px;
  }
}

@media (max-width: 480px) {
  .main-title {
    font-size: 2em;
  }
  
  .parking-icon .icon {
    width: 60px;
    height: 60px;
  }
  
  .description {
    font-size: 1em;
  }
}

/* Loading Animation */
.home {
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Hover Effects */
.content-wrapper:hover .parking-icon {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}

/* Focus States */
.btn:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Additional Visual Polish */
.header-section::after {
  content: '';
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, var(--primary-blue), var(--accent-orange));
  border-radius: 2px;
}

.header-section {
  position: relative;
  padding-bottom: 20px;
}
</style>