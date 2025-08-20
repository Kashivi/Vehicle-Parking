<template>
  <div class="release-spot">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Main Container -->
    <div class="release-container">
      <!-- Header Section -->
      <div class="header-section">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
            <!-- Release Arrow -->
            <path d="M75 35 L85 25 L75 15" stroke="currentColor" stroke-width="2" fill="none"/>
            <line x1="85" y1="25" x2="95" y2="25" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <h2 class="page-title">
          <span class="gradient-text">Release Parking Spot</span>
        </h2>
        <p class="page-subtitle">Complete your parking session</p>
      </div>

      <!-- Form Section (Initial Release Confirmation) -->
      <div v-if="!showDetails" class="form-section">
        <div class="info-card">
          <div class="card-header">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="16" x2="12" y2="12"/>
              <line x1="12" y1="8" x2="12.01" y2="8"/>
            </svg>
            <h3>Release Confirmation</h3>
          </div>
          
          <form @submit.prevent="submitRelease" class="release-form">
            <div class="form-grid">
              <div class="form-group">
                <label for="lot_id" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                    <circle cx="12" cy="10" r="3"/>
                  </svg>
                  Parking Lot
                </label>
                <div class="input-wrapper">
                  <input type="text" id="lot_id" v-model="lot_id" class="form-input" readonly />
                  <div class="input-accent lot-accent"></div>
                </div>
              </div>

              <div class="form-group">
                <label for="spot_id" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                    <path d="M9 9h6v6H9z"/>
                  </svg>
                  Spot Number
                </label>
                <div class="input-wrapper">
                  <input type="text" id="spot_id" v-model="spot_id" class="form-input" readonly />
                  <div class="input-accent spot-accent"></div>
                </div>
              </div>

              <div class="form-group">
                <label for="user_id" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                  </svg>
                  User ID
                </label>
                <div class="input-wrapper">
                  <input type="text" id="user_id" v-model="user_id" class="form-input" readonly />
                  <div class="input-accent user-accent"></div>
                </div>
              </div>
            </div>

            <div class="button-group">
              <button type="submit" class="btn btn-release">
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="9,11 12,14 22,4"/>
                    <path d="M21,12v7a2,2 0 0,1 -2,2H5a2,2 0 0,1 -2,-2V5a2,2 0 0,1 2,-2h11"/>
                  </svg>
                  Confirm Release
                </span>
                <div class="btn-shimmer"></div>
              </button>
              
              <button type="button" class="btn btn-cancel" @click="goToDashboard">
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                  Cancel
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Release Summary Section -->
      <div v-if="showDetails" class="summary-section">
        <div class="success-banner">
          <div class="success-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
              <polyline points="20,6 9,17 4,12"/>
            </svg>
          </div>
          <div class="success-content">
            <h3>Parking Spot Released Successfully!</h3>
            <p>Your parking session has been completed</p>
          </div>
        </div>

        <div class="summary-card">
          <div class="card-header">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14,2 14,8 20,8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
              <polyline points="10,9 9,9 8,9"/>
            </svg>
            <h4>Release Summary</h4>
          </div>

          <div class="summary-grid">
            <div class="summary-item lot-item">
              <div class="item-icon">🏢</div>
              <div class="item-content">
                <span class="item-label">Lot ID</span>
                <span class="item-value">{{ releaseResult.lot_id }}</span>
              </div>
            </div>

            <div class="summary-item spot-item">
              <div class="item-icon">🅿️</div>
              <div class="item-content">
                <span class="item-label">Spot ID</span>
                <span class="item-value">{{ releaseResult.spot_id }}</span>
              </div>
            </div>

            <div class="summary-item user-item">
              <div class="item-icon">👤</div>
              <div class="item-content">
                <span class="item-label">User ID</span>
                <span class="item-value">{{ releaseResult.user_id }}</span>
              </div>
            </div>

            <div class="summary-item time-item">
              <div class="item-icon">⏰</div>
              <div class="item-content">
                <span class="item-label">Parking Time</span>
                <span class="item-value">{{ formatDateTime(releaseResult.parking_timestamp) }}</span>
              </div>
            </div>

            <div class="summary-item release-item">
              <div class="item-icon">🏁</div>
              <div class="item-content">
                <span class="item-label">Release Time</span>
                <span class="item-value">{{ formatDateTime(releaseResult.release_timestamp) }}</span>
              </div>
            </div>

            <div class="summary-item cost-item">
              <div class="item-icon">💰</div>
              <div class="item-content">
                <span class="item-label">Total Cost</span>
                <span class="item-value cost-highlight">₹{{ releaseResult.total_cost }}</span>
              </div>
            </div>
          </div>

          <div class="action-section">
            <button class="btn btn-dashboard" @click="goToDashboard">
              <span class="btn-content">
                <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                  <path d="M9 9h6v6H9z"/>
                </svg>
                Back to Dashboard
              </span>
              <div class="btn-ripple"></div>
            </button>
          </div>
        </div>
      </div>

      <!-- Floating Decorative Elements -->
      <div class="floating-elements">
        <div class="float-shape shape-1"></div>
        <div class="float-shape shape-2"></div>
        <div class="float-shape shape-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReleaseSpot',
  data() {
    return {
      lot_id: this.$route.query.lot_id || '',
      spot_id: this.$route.query.spot_id || '',
      user_id: '',
      releaseResult: null,
      showDetails: false
    };
  },
  created() {
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    this.user_id = user.user_id;
  },
  mounted() {
    this.releaseSpot();  // Automatically call release on mount
  },
  methods: {
    async releaseSpot() {
      const token = localStorage.getItem('auth_token');

      try {
        const res = await fetch('http://localhost:5000/api/release-spot', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `${token}`
          },
          body: JSON.stringify({
            lot_id: this.lot_id,
            spot_id: this.spot_id,
            user_id: this.user_id
          })
        });

        const data = await res.json();

        if (res.ok) {
          this.releaseResult = data;
          this.showDetails = true;
        } else {
          alert('❌ Release failed: ' + data.message);
          this.$router.push('/user-dashboard');
        }

      } catch (error) {
        console.error('Fetch error:', error);
        alert('⚠️ Server error while releasing spot.');
        this.$router.push('/user-dashboard');
      }
    },
    submitRelease() {
      this.releaseSpot();
    },
    formatDateTime(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString();
    },
    goToDashboard() {
      this.$router.push({ path: '/user-dashboard', query: { refresh: 'true' } });
    }
  }
};
</script>

<style scoped>
/* Color Variables - Vibrant Parking Theme */
:root {
  --primary-blue: #2563eb;      
  --secondary-blue: #3b82f6;    
  --accent-orange: #f59e0b;     
  --accent-purple: #8b5cf6;     
  --success-green: #10b981;     
  --pink-accent: #ec4899;       
  --cyan-accent: #06b6d4;       
  --red-accent: #ef4444;        
  --dark-gray: #1f2937;         
  --medium-gray: #6b7280;       
  --light-gray: #f3f4f6;        
  --white: #ffffff;
  --shadow: rgba(0, 0, 0, 0.1);
  --shadow-dark: rgba(0, 0, 0, 0.2);
}

.release-spot {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 25%, 
    var(--pink-accent) 50%, 
    var(--cyan-accent) 75%, 
    var(--success-green) 100%);
  background-size: 400% 400%;
  animation: gradientShift 12s ease infinite;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Animated Background Pattern */
.bg-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(245, 158, 11, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.08) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 100px,
      rgba(255, 255, 255, 0.02) 102px,
      rgba(255, 255, 255, 0.02) 104px
    );
  animation: drift 25s linear infinite, pulse 8s ease-in-out infinite;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(50px, 50px) rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}

/* Main Container */
.release-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 700px;
  width: 100%;
  box-shadow: 
    0 30px 100px var(--shadow-dark),
    0 0 0 1px rgba(255, 255, 255, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.3);
  position: relative;
  z-index: 1;
  animation: slideUp 0.8s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Header Section */
.header-section {
  text-align: center;
  margin-bottom: 40px;
  position: relative;
}

.parking-icon {
  display: inline-block;
  margin-bottom: 20px;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 4s ease-in-out infinite, iconGlow 6s ease infinite;
}

.parking-icon .icon {
  width: 70px;
  height: 70px;
  filter: drop-shadow(0 4px 15px rgba(16, 185, 129, 0.3));
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes iconGlow {
  0%, 100% { filter: drop-shadow(0 4px 15px rgba(16, 185, 129, 0.3)) hue-rotate(0deg); }
  33% { filter: drop-shadow(0 4px 15px rgba(6, 182, 212, 0.3)) hue-rotate(120deg); }
  66% { filter: drop-shadow(0 4px 15px rgba(245, 158, 11, 0.3)) hue-rotate(240deg); }
}

.page-title {
  font-size: 2.5em;
  font-weight: 800;
  margin-bottom: 10px;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000; /* solid black */
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.2); /* subtle glow */
}

@keyframes textFlow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.page-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

/* Form Section */
.info-card {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(243, 244, 246, 0.8));
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
  overflow: hidden;
}

.info-card::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 2px solid var(--light-gray);
}

.card-icon {
  width: 24px;
  height: 24px;
  color: var(--success-green);
}

.card-header h3,
.card-header h4 {
  margin: 0;
  font-weight: 700;
  color: var(--dark-gray);
}

/* Form Grid */
.form-grid {
  display: grid;
  gap: 20px;
  margin-bottom: 30px;
}

.form-group {
  position: relative;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: var(--dark-gray);
  margin-bottom: 8px;
  font-size: 0.95em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.label-icon {
  width: 16px;
  height: 16px;
  color: var(--primary-blue);
}

.input-wrapper {
  position: relative;
}

.form-input {
  width: 100%;
  padding: 16px 20px;
  border: 2px solid var(--light-gray);
  border-radius: 12px;
  background: var(--white);
  font-size: 1em;
  font-weight: 600;
  color: var(--dark-gray);
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px var(--shadow);
  outline: none;
}

.form-input:focus {
  border-color: transparent;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.2);
}

.input-accent {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 100%;
  border-radius: 0 0 12px 12px;
  opacity: 0.8;
}

.lot-accent {
  background: linear-gradient(90deg, var(--success-green), var(--cyan-accent));
}

.spot-accent {
  background: linear-gradient(90deg, var(--accent-orange), var(--pink-accent));
}

.user-accent {
  background: linear-gradient(90deg, var(--accent-purple), var(--primary-blue));
}

/* Button Styling */
.button-group {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 16px 32px;
  border: none;
  border-radius: 12px;
  font-size: 1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  min-width: 160px;
}

.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.btn-release {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);
}

.btn-release:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 60px rgba(16, 185, 129, 0.6);
}

.btn-cancel {
  background: linear-gradient(135deg, var(--medium-gray), var(--dark-gray));
  color: var(--white);
  box-shadow: 0 10px 40px rgba(107, 114, 128, 0.3);
}

.btn-cancel:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 60px rgba(107, 114, 128, 0.5);
}

.btn-dashboard {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple), var(--pink-accent));
  background-size: 300% 300%;
  color: var(--white);
  box-shadow: 0 10px 40px rgba(37, 99, 235, 0.4);
  animation: dashboardGlow 4s ease-in-out infinite;
  width: 100%;
  max-width: 300px;
}

@keyframes dashboardGlow {
  0%, 100% { 
    background-position: 0% 50%;
    box-shadow: 0 10px 40px rgba(37, 99, 235, 0.4);
  }
  50% { 
    background-position: 100% 50%;
    box-shadow: 0 10px 40px rgba(139, 92, 246, 0.6);
  }
}

.btn-dashboard:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 20px 80px rgba(139, 92, 246, 0.7);
}

.btn-shimmer,
.btn-ripple {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.2), 
    transparent);
  transition: left 0.6s ease;
  z-index: 1;
}

.btn:hover .btn-shimmer,
.btn:hover .btn-ripple {
  left: 100%;
}

.btn:hover .btn-icon {
  transform: scale(1.1);
}

/* Success Banner */
.success-banner {
  display: flex;
  align-items: center;
  gap: 20px;
  background: linear-gradient(135deg, 
    rgba(16, 185, 129, 0.1), 
    rgba(6, 182, 212, 0.1));
  border: 2px solid var(--success-green);
  border-radius: 16px;
  padding: 25px;
  margin-bottom: 30px;
  animation: successPulse 2s ease-in-out infinite;
}

@keyframes successPulse {
  0%, 100% { 
    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4);
    border-color: var(--success-green);
  }
  50% { 
    box-shadow: 0 0 0 10px rgba(16, 185, 129, 0);
    border-color: var(--cyan-accent);
  }
}

.success-icon {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  border-radius: 50%;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.success-icon svg {
  width: 24px;
  height: 24px;
  color: var(--white);
}

.success-content h3 {
  margin: 0 0 5px 0;
  color: var(--success-green);
  font-weight: 700;
  font-size: 1.3em;
}

.success-content p {
  margin: 0;
  color: var(--medium-gray);
  font-weight: 500;
}

/* Summary Grid */
.summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.summary-item {
  display: flex;
  align-items: center;
  gap: 15px;
  background: linear-gradient(145deg, var(--white), rgba(243, 244, 246, 0.5));
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 8px 25px var(--shadow);
  border: 2px solid transparent;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.summary-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.1), 
    transparent);
  transition: left 0.5s ease;
}

.summary-item:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 15px 50px var(--shadow-dark);
}

.summary-item:hover::before {
  left: 100%;
}

.lot-item { border-color: var(--success-green); }
.spot-item { border-color: var(--accent-orange); }
.user-item { border-color: var(--accent-purple); }
.time-item { border-color: var(--cyan-accent); }
.release-item { border-color: var(--pink-accent); }
.cost-item { 
  border-color: var(--accent-orange); 
  background: linear-gradient(145deg, rgba(245, 158, 11, 0.05), rgba(236, 72, 153, 0.05));
}

.item-icon {
  font-size: 2em;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  border-radius: 12px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 50px;
  height: 50px;
  box-shadow: 0 4px 15px var(--shadow);
}

.item-content {
  flex: 1;
}

.item-label {
  display: block;
  font-size: 0.85em;
  color: var(--medium-gray);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.item-value {
  display: block;
  font-size: 1.1em;
  font-weight: 700;
  color: var(--dark-gray);
}

.cost-highlight {
  font-size: 1.3em;
  font-weight: 900;
  color: #000; /* solid black */
}


/* Action Section */
.action-section {
  text-align: center;
  padding-top: 20px;
  border-top: 2px solid rgba(107, 114, 128, 0.1);
}

/* Floating Decorative Elements */
.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.float-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: 5%;
  right: 5%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatAround 12s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: 10%;
  left: 8%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatAround 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 100px;
  height: 100px;
  top: 40%;
  right: 15%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatAround 15s ease-in-out infinite;
}

@keyframes floatAround {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(20px, -20px) rotate(90deg); }
  50% { transform: translate(-15px, -30px) rotate(180deg); }
  75% { transform: translate(-25px, 15px) rotate(270deg); }
}

/* Summary Card Specific Styling */
.summary-card {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(243, 244, 246, 0.9));
  border-radius: 20px;
  padding: 35px;
  box-shadow: 0 20px 60px var(--shadow-dark);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
  overflow: hidden;
}

.summary-card::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, 
    var(--success-green), 
    var(--cyan-accent), 
    var(--accent-orange), 
    var(--pink-accent));
  background-size: 400% 400%;
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  animation: borderFlow 6s ease infinite;
}

@keyframes borderFlow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

/* Responsive Design */
@media (max-width: 768px) {
  .release-container {
    padding: 40px 25px;
    margin: 10px;
  }
  
  .page-title {
    font-size: 2em;
  }
  
  .summary-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .button-group {
    flex-direction: column;
    align-items: center;
  }
  
  .btn {
    width: 100%;
    max-width: 280px;
  }
  
  .success-banner {
    flex-direction: column;
    text-align: center;
    gap: 15px;
  }
}

@media (max-width: 480px) {
  .release-container {
    padding: 30px 20px;
  }
  
  .page-title {
    font-size: 1.8em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
  
  .summary-item {
    padding: 15px;
  }
  
  .item-icon {
    font-size: 1.5em;
    padding: 8px;
    min-width: 40px;
    height: 40px;
  }
}

/* Loading States */
.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  animation: none;
}

/* Focus States for Accessibility */
.btn:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Enhanced Animations */
.form-section {
  animation: fadeInLeft 0.8s ease-out 0.2s both;
}

.summary-section {
  animation: fadeInRight 0.8s ease-out 0.2s both;
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Interactive Hover Effects */
.summary-item:hover .item-icon {
  transform: scale(1.1) rotate(5deg);
  transition: transform 0.3s ease;
}

.form-group:hover .label-icon {
  color: var(--accent-orange);
  transform: scale(1.1);
  transition: all 0.3s ease;
}

/* Additional Polish */
.header-section::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(90deg, 
    var(--success-green), 
    var(--cyan-accent), 
    var(--accent-orange));
  border-radius: 2px;
  animation: lineGlow 3s ease infinite;
}

@keyframes lineGlow {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}
</style>