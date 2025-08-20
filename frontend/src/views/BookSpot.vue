<template>
  <div class="book-spot">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Book Spot Container -->
    <div class="book-spot-container">
      <!-- Header Section -->
      <div class="book-spot-header">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
          </svg>
        </div>
        <h1 class="book-spot-title">
          <span class="gradient-text">Reserve Your Spot</span>
        </h1>
        <p class="book-spot-subtitle">Secure your parking space in seconds</p>
      </div>

      <!-- Parking Details Section -->
      <div class="info-section">
        <h3 class="section-title">
          <svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
            <line x1="8" y1="21" x2="16" y2="21"/>
            <line x1="12" y1="17" x2="12" y2="21"/>
          </svg>
          Parking Details
        </h3>
        <div class="info-grid">
          <div class="info-card">
            <div class="info-label">
              <svg class="info-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
              Lot ID
            </div>
            <div class="info-value">{{ lot_id || 'Loading...' }}</div>
            <div class="info-shimmer"></div>
          </div>
          
          <div class="info-card spot-card">
            <div class="info-label">
              <svg class="info-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
              </svg>
              Assigned Spot
            </div>
            <div class="info-value spot-highlight">{{ spot_id || 'Finding spot...' }}</div>
            <div class="info-shimmer"></div>
          </div>
          
          <div class="info-card">
            <div class="info-label">
              <svg class="info-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <circle cx="12" cy="7" r="4"/>
              </svg>
              User ID
            </div>
            <div class="info-value">{{ user_id || 'Loading...' }}</div>
            <div class="info-shimmer"></div>
          </div>
        </div>
      </div>

      <!-- Booking Form -->
      <form @submit.prevent="submitBooking" class="book-spot-form">
        <!-- Vehicle Input -->
        <div class="form-group">
          <label for="vehicleNumber" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M7 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/>
              <path d="M17 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/>
              <path d="M5 17h-2v-6l2-5h9l4 5h1a2 2 0 0 1 2 2v4h-2"/>
              <path d="M9 17v-6h6v6"/>
              <path d="M9 5v6"/>
              <path d="M15 5v6"/>
            </svg>
            Vehicle License Plate
          </label>
          <div class="input-wrapper">
            <input 
              v-model="vehicle_number" 
              type="text" 
              id="vehicleNumber"
              class="form-input"
              placeholder="Enter your license plate number"
              required
              :disabled="isSubmitting"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="button-group">
          <button type="submit" class="btn-reserve" :disabled="isSubmitting">
            <span class="btn-content">
              <svg v-if="!isSubmitting" class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20,6 9,17 4,12"/>
              </svg>
              <div v-else class="loading-spinner"></div>
              {{ isSubmitting ? 'Reserving...' : 'Reserve Spot' }}
            </span>
            <div class="btn-shimmer"></div>
          </button>
          
          <button type="button" class="btn-cancel" @click="cancel" :disabled="isSubmitting">
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

      <!-- Decorative Elements -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
    </div>

    <!-- Loading overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner large"></div>
        <p class="loading-text">Finding available spot...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookSpot',
  data() {
    return {
      lot_id: null,
      spot_id: null,
      user_id: null,
      vehicle_number: '',
      isLoading: true,
      isSubmitting: false,
    };
  },
  async created() {
    try {
      // Fetch user info from localStorage
      const tokenData = JSON.parse(localStorage.getItem('user') || '{}');
      this.user_id = tokenData.user_id;
      
      this.lot_id = this.$route.query.lot_id;
      
      const token = localStorage.getItem('auth_token');
      const response = await fetch(`http://localhost:5000/api/available-spot?lot_id=${this.lot_id}`, {
        headers: {
          'Authorization': `${token}`
        }
      });
      
      const data = await response.json();
      
      if (response.ok && data.spot_number) {
        this.spot_id = data.spot_number;
      } else {
        this.showAlert('No available spot found in the selected lot.', 'warning');
        this.$router.push('/user-dashboard');
      }
    } catch (err) {
      console.error('Error fetching spot:', err);
      this.showAlert('Error contacting server. Please login again or try later.', 'error');
      this.$router.push('/user-dashboard');
    } finally {
      this.isLoading = false;
    }
  },
  methods: {
    async submitBooking() {
      this.isSubmitting = true;
      
      try {
        const token = localStorage.getItem('auth_token');
        const response = await fetch('http://localhost:5000/api/book-spot', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `${token}`
          },
          body: JSON.stringify({
            lot_id: this.lot_id,
            spot_id: this.spot_id,
            user_id: this.user_id,
            vehicle_number: this.vehicle_number
          })
        });
        
        const result = await response.json();
        
        if (response.ok) {
          this.showAlert('Spot booked successfully!', 'success');
          setTimeout(() => {
            this.$router.push('/user-dashboard');
          }, 1500);
        } else {
          this.showAlert('Booking failed: ' + (result.message || 'Unknown error'), 'error');
        }
      } catch (error) {
        console.error('Booking error:', error);
        this.showAlert('Server error. Please try again later.', 'error');
      } finally {
        this.isSubmitting = false;
      }
    },
    
    cancel() {
      this.$router.push('/user-dashboard');
    },
    
    showAlert(message, type) {
      // Create and show custom alert
      const alertDiv = document.createElement('div');
      alertDiv.className = `custom-alert alert-${type}`;
      alertDiv.innerHTML = `
        <div class="alert-content">
          <span class="alert-icon">
            ${type === 'success' ? '✅' : type === 'warning' ? '⚠️' : '❌'}
          </span>
          <span class="alert-message">${message}</span>
        </div>
      `;
      
      document.body.appendChild(alertDiv);
      
      // Animate in
      setTimeout(() => alertDiv.classList.add('show'), 100);
      
      // Remove after 3 seconds
      setTimeout(() => {
        alertDiv.classList.remove('show');
        setTimeout(() => document.body.removeChild(alertDiv), 300);
      }, 3000);
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

.book-spot {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--accent-purple) 0%, 
    var(--primary-blue) 25%, 
    var(--cyan-accent) 50%, 
    var(--success-green) 75%, 
    var(--accent-orange) 100%);
  background-size: 400% 400%;
  animation: gradientShift 10s ease infinite;
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
    radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(245, 158, 11, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 60% 20%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 80px,
      rgba(255, 255, 255, 0.02) 82px,
      rgba(255, 255, 255, 0.02) 84px
    );
  animation: drift 20s linear infinite, pulse 6s ease-in-out infinite;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(30px, 30px) rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}

/* Book Spot Container */
.book-spot-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 520px;
  width: 100%;
  box-shadow: 
    0 25px 80px var(--shadow-dark),
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
.book-spot-header {
  text-align: center;
  margin-bottom: 40px;
}

.parking-icon {
  display: inline-block;
  margin-bottom: 20px;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 4s ease-in-out infinite, colorRotate 8s ease infinite;
}

.parking-icon .icon {
  width: 60px;
  height: 60px;
  filter: drop-shadow(0 4px 12px rgba(245, 158, 11, 0.4));
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

@keyframes colorRotate {
  0%, 100% { filter: drop-shadow(0 4px 12px rgba(245, 158, 11, 0.4)) hue-rotate(0deg); }
  33% { filter: drop-shadow(0 4px 12px rgba(236, 72, 153, 0.4)) hue-rotate(120deg); }
  66% { filter: drop-shadow(0 4px 12px rgba(139, 92, 246, 0.4)) hue-rotate(240deg); }
}

.book-spot-title {
  font-size: 2.4em;
  font-weight: 800;
  margin-bottom: 8px;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000; /* solid black */
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.2); /* subtle glow */
}

@keyframes textShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.book-spot-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

/* Info Section */
.info-section {
  margin-bottom: 35px;
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.3em;
  font-weight: 700;
  color: var(--dark-gray);
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section-icon {
  width: 24px;
  height: 24px;
  color: var(--accent-orange);
  animation: iconPulse 2s ease-in-out infinite;
}

@keyframes iconPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
}

.info-card {
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.9) 0%, 
    rgba(243, 244, 246, 0.9) 100%);
  border: 2px solid transparent;
  background-clip: padding-box;
  border-radius: 16px;
  padding: 20px;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px var(--shadow);
}

.info-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, 
    var(--accent-orange), 
    var(--pink-accent), 
    var(--accent-purple));
  border-radius: 16px;
  z-index: -1;
  margin: -2px;
}

.spot-card {
  background: linear-gradient(135deg, 
    rgba(16, 185, 129, 0.1) 0%, 
    rgba(6, 182, 212, 0.1) 100%);
  border: 2px solid var(--success-green);
}

.spot-card::before {
  background: linear-gradient(135deg, 
    var(--success-green), 
    var(--cyan-accent));
}

.info-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px var(--shadow-dark);
}

.info-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9em;
  font-weight: 600;
  color: var(--medium-gray);
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.info-icon {
  width: 16px;
  height: 16px;
  color: var(--accent-orange);
}

.info-value {
  font-size: 1.2em;
  font-weight: 700;
  color: var(--dark-gray);
  position: relative;
}

.spot-highlight {
  font-size: 1.4em;
  font-weight: 600;
  color: #000; /* solid black */
  animation: spotPulse 2s ease-in-out infinite;
}

@keyframes spotPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.info-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.3), 
    transparent);
  animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
  0% { left: -100%; }
  100% { left: 100%; }
}

/* Form Styling */
.book-spot-form {
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.form-group {
  margin-bottom: 30px;
  position: relative;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: var(--dark-gray);
  margin-bottom: 12px;
  font-size: 1em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.label-icon {
  width: 20px;
  height: 20px;
  color: var(--accent-orange);
  transition: all 0.3s ease;
}

.input-wrapper {
  position: relative;
}

.form-input {
  width: 100%;
  padding: 20px 24px;
  border: 2px solid transparent;
  border-radius: 16px;
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--accent-orange), var(--pink-accent), var(--accent-purple)) border-box;
  font-size: 1.1em;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 8px 30px var(--shadow);
  outline: none;
  position: relative;
  z-index: 2;
}

.form-input:focus {
  transform: translateY(-3px);
  box-shadow: 0 15px 50px rgba(245, 158, 11, 0.4);
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--primary-blue)) border-box;
}

.form-input::placeholder {
  color: var(--medium-gray);
  opacity: 0.7;
}

.form-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.input-border {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--success-green), var(--cyan-accent), var(--primary-blue));
  border-radius: 0 0 16px 16px;
  transition: width 0.4s ease;
}

.form-input:focus + .input-border {
  width: 100%;
}

/* Button Group */
.button-group {
  display: flex;
  gap: 15px;
  margin-top: 35px;
}

/* Reserve Button */
.btn-reserve {
  flex: 2;
  padding: 20px 28px;
  background: linear-gradient(135deg, 
    var(--success-green) 0%, 
    var(--cyan-accent) 50%, 
    var(--primary-blue) 100%);
  background-size: 300% 300%;
  color: var(--white);
  border: none;
  border-radius: 16px;
  font-size: 1.1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 12px 50px rgba(16, 185, 129, 0.5);
  animation: buttonGlow 3s ease-in-out infinite;
}

/* Cancel Button */
.btn-cancel {
  flex: 1;
  padding: 20px 28px;
  background: linear-gradient(135deg, 
    var(--medium-gray) 0%, 
    var(--dark-gray) 100%);
  color: var(--white);
  border: none;
  border-radius: 16px;
  font-size: 1.1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 12px 50px rgba(107, 114, 128, 0.3);
}

@keyframes buttonGlow {
  0%, 100% { 
    background-position: 0% 50%;
    box-shadow: 0 12px 50px rgba(16, 185, 129, 0.5);
  }
  50% { 
    background-position: 100% 50%;
    box-shadow: 0 12px 50px rgba(6, 182, 212, 0.7);
  }
}

.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 22px;
  height: 22px;
  transition: transform 0.3s ease;
}

.btn-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.3), 
    transparent);
  transition: left 0.6s ease;
  z-index: 1;
}

.btn-reserve:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 70px rgba(6, 182, 212, 0.8);
  background-position: 100% 50%;
}

.btn-cancel:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 70px rgba(107, 114, 128, 0.6);
  background: linear-gradient(135deg, 
    var(--dark-gray) 0%, 
    var(--medium-gray) 100%);
}

.btn-reserve:hover .btn-shimmer {
  left: 100%;
}

.btn-reserve:hover .btn-icon,
.btn-cancel:hover .btn-icon {
  transform: translateX(4px);
}

.btn-reserve:active,
.btn-cancel:active {
  transform: translateY(-2px);
}

.btn-reserve:disabled,
.btn-cancel:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  animation: none;
}

/* Loading Spinner */
.loading-spinner {
  width: 22px;
  height: 22px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top: 3px solid var(--white);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.loading-spinner.large {
  width: 40px;
  height: 40px;
  border-width: 4px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease;
}

.loading-content {
  text-align: center;
  color: var(--white);
}

.loading-text {
  margin-top: 20px;
  font-size: 1.2em;
  font-weight: 500;
  opacity: 0.9;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Floating Decorative Shapes */
.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.1;
}

.shape-1 {
  width: 80px;
  height: 80px;
  top: 10%;
  right: 10%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatShape 8s ease-in-out infinite;
}

.shape-2 {
  width: 60px;
  height: 60px;
  bottom: 20%;
  left: 15%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatShape 6s ease-in-out infinite reverse;
}

.shape-3 {
  width: 100px;
  height: 100px;
  top: 50%;
  right: 5%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatShape 10s ease-in-out infinite;
}

@keyframes floatShape {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(25px, -20px) rotate(90deg); }
  50% { transform: translate(-15px, -30px) rotate(180deg); }
  75% { transform: translate(-25px, 15px) rotate(270deg); }
}

/* Custom Alert Styles */
.custom-alert {
  position: fixed;
  top: 30px;
  right: 30px;
  background: var(--white);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 15px 50px var(--shadow-dark);
  z-index: 10000;
  transform: translateX(400px);
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  backdrop-filter: blur(15px);
  border: 2px solid transparent;
  min-width: 300px;
}

.custom-alert.show {
  transform: translateX(0);
  opacity: 1;
}

.alert-success {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(255, 255, 255, 0.95));
  border-color: var(--success-green);
}

.alert-warning {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(255, 255, 255, 0.95));
  border-color: var(--accent-orange);
}

.alert-error {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(255, 255, 255, 0.95));
  border-color: var(--red-accent);
}

.alert-content {
  display: flex;
  align-items: center;
  gap: 15px;
}

.alert-icon {
  font-size: 1.5em;
  flex-shrink: 0;
}

.alert-message {
  font-weight: 600;
  color: var(--dark-gray);
  font-size: 1em;
}

/* Animation for form elements */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .book-spot-container {
    padding: 40px 25px;
    margin: 15px;
    max-width: 400px;
  }
  
  .book-spot-title {
    font-size: 2em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
  
  .info-grid {
    gap: 12px;
  }
  
  .info-card {
    padding: 16px;
  }
  
  .button-group {
    flex-direction: column;
    gap: 12px;
  }
  
  .btn-reserve,
  .btn-cancel {
    flex: none;
    padding: 18px 24px;
  }
  
  .custom-alert {
    right: 15px;
    left: 15px;
    min-width: auto;
  }
}

@media (max-width: 480px) {
  .book-spot {
    padding: 15px;
  }
  
  .book-spot-container {
    padding: 30px 20px;
    border-radius: 20px;
  }
  
  .book-spot-title {
    font-size: 1.8em;
  }
  
  .section-title {
    font-size: 1.1em;
  }
  
  .info-card {
    padding: 14px;
  }
  
  .info-value {
    font-size: 1.1em;
  }
  
  .spot-highlight {
    font-size: 1.2em;
  }
  
  .form-input {
    padding: 16px 20px;
    font-size: 1em;
  }
  
  .btn-reserve,
  .btn-cancel {
    padding: 16px 20px;
    font-size: 1em;
  }
  
  .custom-alert {
    top: 20px;
    right: 10px;
    left: 10px;
    padding: 16px;
  }
}

/* Focus States for Accessibility */
.btn-reserve:focus,
.btn-cancel:focus,
.form-input:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 3px;
}

/* Interactive Hover Effects */
.book-spot-container:hover .parking-icon {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}

.form-group:hover .label-icon {
  color: var(--pink-accent);
  transform: scale(1.15);
  transition: all 0.3s ease;
}

/* Enhanced loading states */
.loading-content {
  animation: fadeInUp 0.6s ease-out;
}

/* Subtle animations for better UX */
.info-card {
  animation: fadeInUp 0.6s ease-out;
}

.info-card:nth-child(1) { animation-delay: 0.1s; }
.info-card:nth-child(2) { animation-delay: 0.2s; }
.info-card:nth-child(3) { animation-delay: 0.3s; }

/* Enhanced spot highlight effect */
.spot-card:hover .spot-highlight {
  animation: spotGlow 1s ease-in-out;
}

@keyframes spotGlow {
  0%, 100% { 
    filter: drop-shadow(0 0 0 transparent);
  }
  50% { 
    filter: drop-shadow(0 0 20px rgba(16, 185, 129, 0.6));
  }
}

/* Improved loading overlay */
.loading-overlay {
  animation: overlayFadeIn 0.4s ease-out;
}

@keyframes overlayFadeIn {
  from {
    opacity: 0;
    backdrop-filter: blur(0px);
  }
  to {
    opacity: 1;
    backdrop-filter: blur(10px);
  }
}

/* Enhanced button interactions */
.btn-reserve::before,
.btn-cancel::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.6s ease;
}

.btn-reserve:active::before,
.btn-cancel:active::before {
  width: 300px;
  height: 300px;
}
</style>