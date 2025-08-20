<template>
  <div class="add-lot">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Add Lot Container -->
    <div class="add-lot-container">
      <!-- Header Section -->
      <div class="add-lot-header">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="15" width="80" height="70" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="25" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="38" y="25" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="56" y="25" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="74" y="25" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="20" y="50" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="38" y="50" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="56" y="50" width="12" height="20" rx="2" fill="currentColor"/>
            <rect x="74" y="50" width="12" height="20" rx="2" fill="currentColor"/>
            <circle cx="50" cy="78" r="3" fill="currentColor"/>
            <text x="50" y="83" text-anchor="middle" font-size="8" fill="currentColor" font-weight="bold">+</text>
          </svg>
        </div>
        <h1 class="add-lot-title">
          <span class="gradient-text">Create New Parking Lot</span>
        </h1>
        <p class="add-lot-subtitle">Build the perfect parking solution</p>
      </div>

      <!-- Add Lot Form -->
      <form @submit.prevent="addLot" class="add-lot-form">
        <!-- Location Name Input -->
        <div class="form-group">
          <label for="locationName" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
              <circle cx="12" cy="10" r="3"/>
            </svg>
            Prime Location Name
          </label>
          <div class="input-wrapper">
            <input 
              v-model="lot.prime_location_name" 
              type="text" 
              id="locationName"
              class="form-input"
              placeholder="Enter prime location name"
              required
              :disabled="isSubmitting"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Address Input -->
        <div class="form-group">
          <label for="address" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9,22 9,12 15,12 15,22"/>
            </svg>
            Complete Address
          </label>
          <div class="input-wrapper">
            <textarea 
              v-model="lot.address" 
              id="address"
              class="form-input form-textarea"
              placeholder="Enter detailed address"
              rows="3"
              required
              :disabled="isSubmitting"
            ></textarea>
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Pin Code Input -->
        <div class="form-group">
          <label for="pinCode" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 2L2 7v10c0 5.55 3.84 10 9 11 5.16-1 9-5.45 9-11V7l-10-5z"/>
              <path d="M9 12l2 2 4-4"/>
            </svg>
            Pin Code
          </label>
          <div class="input-wrapper">
            <input 
              v-model="lot.pin_code" 
              type="text" 
              id="pinCode"
              class="form-input"
              placeholder="Enter pin code"
              required
              :disabled="isSubmitting"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Price and Spots Row -->
        <div class="form-row">
          <!-- Price Input -->
          <div class="form-group">
            <label for="price" class="form-label">
              <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="12" y1="1" x2="12" y2="23"/>
                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
              </svg>
              Price per Hour
            </label>
            <div class="input-wrapper">
              <input 
                v-model="lot.price" 
                type="number" 
                id="price"
                class="form-input"
                placeholder="₹ 0.00"
                min="0"
                step="0.01"
                required
                :disabled="isSubmitting"
              />
              <div class="input-border"></div>
            </div>
          </div>

          <!-- Number of Spots Input -->
          <div class="form-group">
            <label for="maxSpots" class="form-label">
              <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
              </svg>
              Total Spots
            </label>
            <div class="input-wrapper">
              <input 
                v-model="lot.number_of_spots" 
                type="number" 
                id="maxSpots"
                class="form-input"
                placeholder="Number of spots"
                min="1"
                required
                :disabled="isSubmitting"
              />
              <div class="input-border"></div>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="button-group">
          <button type="submit" class="btn-create" :disabled="isSubmitting">
            <span class="btn-content">
              <svg v-if="!isSubmitting" class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20,6 9,17 4,12"/>
              </svg>
              <div v-else class="loading-spinner"></div>
              {{ isSubmitting ? 'Creating...' : 'Create Parking Lot' }}
            </span>
            <div class="btn-shimmer"></div>
          </button>
          
          <button type="button" class="btn-cancel" @click="goBack" :disabled="isSubmitting">
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

      <!-- Preview Card -->
      <div class="preview-section" v-if="hasPreviewData">
        <h3 class="section-title">
          <svg class="section-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
            <circle cx="12" cy="12" r="3"/>
          </svg>
          Live Preview
        </h3>
        <div class="preview-card">
          <div class="preview-header">
            <h4>{{ lot.prime_location_name || 'Location Name' }}</h4>
            <div class="preview-price">₹{{ lot.price || '0' }}/hr</div>
          </div>
          <p class="preview-address">{{ lot.address || 'Address will appear here' }}</p>
          <div class="preview-details">
            <span class="preview-pin">{{ lot.pin_code || 'PIN' }}</span>
            <span class="preview-spots">{{ lot.number_of_spots || '0' }} spots</span>
          </div>
        </div>
      </div>

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
        <p class="loading-text">Creating parking lot...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddParkingLot',
  data() {
    return {
      lot: {
        prime_location_name: "",
        address: "",
        pin_code: "",
        price: "",
        number_of_spots: ""
      },
      isSubmitting: false,
      isLoading: false
    };
  },
  computed: {
    hasPreviewData() {
      return this.lot.prime_location_name || this.lot.address || this.lot.price || this.lot.number_of_spots;
    }
  },
  methods: {
    async addLot() {
      this.isSubmitting = true;
      this.isLoading = true;
      
      try {
        const response = await fetch('http://localhost:5000/api/parkinglot', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.lot)
        });

        if (response.ok) {
          this.showAlert('Parking lot created successfully!', 'success');
          setTimeout(() => {
            this.$router.push("/admin-dashboard");
          }, 1500);
        } else {
          const err = await response.json();
          this.showAlert('Error: ' + (err.message || 'Failed to create parking lot'), 'error');
        }
      } catch (err) {
        console.error(err);
        this.showAlert('Server error. Please try again later.', 'error');
      } finally {
        this.isSubmitting = false;
        this.isLoading = false;
      }
    },
    
    goBack() {
      this.$router.push('/admin-dashboard');
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

.add-lot {
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

/* Add Lot Container */
.add-lot-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 600px;
  width: 100%;
  box-shadow: 
    0 25px 80px var(--shadow-dark),
    0 0 0 1px rgba(255, 255, 255, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.3);
  position: relative;
  z-index: 1;
  animation: slideUp 0.8s ease-out;
  max-height: 90vh;
  overflow-y: auto;
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
.add-lot-header {
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

.add-lot-title {
  font-size: 2.4em;
  font-weight: 800;
  margin-bottom: 8px;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000;
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}

.add-lot-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

/* Form Styling */
.add-lot-form {
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.form-group {
  margin-bottom: 25px;
  position: relative;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    width: 100%; 
  }
  .form-row .form-group {
    min-width: 0; /* This prevents overflow issues */
  }

  @media (max-width: 768px) {
    .form-row {
      grid-template-columns: 1fr; /* Stack on smaller screens */
      gap: 15px;
    }
    
    /* Ensure form groups take full width when stacked */
    .form-row .form-group {
      width: 100%;
    }
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
  padding: 18px 20px;
  border: 2px solid transparent;
  border-radius: 16px;
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--accent-orange), var(--pink-accent), var(--accent-purple)) border-box;
  font-size: 1em;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 8px 30px var(--shadow);
  outline: none;
  position: relative;
  z-index: 2;
  resize: none;
}

.form-textarea {
  min-height: 80px;
  resize: vertical;
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

/* Create Button */
.btn-create {
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

.btn-create:hover {
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

.btn-create:hover .btn-shimmer {
  left: 100%;
}

.btn-create:hover .btn-icon,
.btn-cancel:hover .btn-icon {
  transform: translateX(4px);
}

.btn-create:active,
.btn-cancel:active {
  transform: translateY(-2px);
}

.btn-create:disabled,
.btn-cancel:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  animation: none;
}

/* Preview Section */
.preview-section {
  margin-top: 30px;
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.2em;
  font-weight: 700;
  color: var(--dark-gray);
  margin-bottom: 15px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section-icon {
  width: 20px;
  height: 20px;
  color: var(--accent-orange);
  animation: iconPulse 2s ease-in-out infinite;
}

@keyframes iconPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.preview-card {
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.9) 0%, 
    rgba(243, 244, 246, 0.9) 100%);
  border: 2px solid transparent;
  background-clip: padding-box;
  border-radius: 16px;
  padding: 20px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 25px var(--shadow);
  transition: all 0.3s ease;
}

.preview-card::before {
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

.preview-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px var(--shadow-dark);
}

.preview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.preview-header h4 {
  font-size: 1.3em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0;
}

.preview-price {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  padding: 6px 12px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9em;
}

.preview-address {
  color: var(--medium-gray);
  margin-bottom: 12px;
  font-size: 0.95em;
  line-height: 1.4;
}

.preview-details {
  display: flex;
  gap: 15px;
  align-items: center;
}

.preview-pin,
.preview-spots {
  background: rgba(107, 114, 128, 0.1);
  color: var(--medium-gray);
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.85em;
  font-weight: 500;
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

/* Enhanced interactive effects */
.form-group:hover .label-icon {
  color: var(--pink-accent);
  transform: scale(1.15);
  transition: all 0.3s ease;
}

/* Responsive Design */
@media (max-width: 768px) {
  .add-lot-container {
    padding: 40px 25px;
    margin: 15px;
    max-width: 400px;
  }
  
  .add-lot-title {
    font-size: 2em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
  
  
  .button-group {
    flex-direction: column;
    gap: 12px;
  }
  
  .btn-create,
  .btn-cancel {
    flex: none;
    padding: 18px 24px;
  }
  
  .custom-alert {
    right: 15px;
    left: 15px;
    min-width: auto;
  }
  
  .preview-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  
  .preview-details {
    flex-wrap: wrap;
    gap: 10px;
  }
}

@media (max-width: 480px) {
  .add-lot {
    padding: 15px;
  }
  
  .add-lot-container {
    padding: 30px 20px;
    border-radius: 20px;
  }
  
  .add-lot-title {
    font-size: 1.8em;
  }
  
  .section-title {
    font-size: 1.1em;
  }
  
  .form-input {
    padding: 16px 18px;
    font-size: 0.95em;
  }
  
  .form-textarea {
    min-height: 70px;
  }
  
  .btn-create,
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
  
  .preview-card {
    padding: 16px;
  }
  
  .preview-header h4 {
    font-size: 1.1em;
  }
}

/* Focus States for Accessibility */
.btn-create:focus,
.btn-cancel:focus,
.form-input:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 3px;
}

/* Enhanced button interactions */
.btn-create::before,
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

.btn-create:active::before,
.btn-cancel:active::before {
  width: 300px;
  height: 300px;
}

/* Smooth scrollbar for container */
.add-lot-container::-webkit-scrollbar {
  width: 8px;
}

.add-lot-container::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
}

.add-lot-container::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  border-radius: 10px;
}

.add-lot-container::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, var(--pink-accent), var(--accent-purple));
}

/* Enhanced preview animations */
.preview-card {
  animation: fadeInUp 0.6s ease-out 0.6s both;
}

/* Input validation feedback */
.form-input:valid {
  border-color: var(--success-green);
}

.form-input:invalid:not(:placeholder-shown) {
  border-color: var(--red-accent);
}

/* Improved loading states */
.loading-content {
  animation: fadeInUp 0.6s ease-out;
}

/* Enhanced loading overlay */
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

/* Subtle hover effects for better UX */
.add-lot-container:hover .parking-icon {
  transform: scale(1.05);
  transition: transform 0.3s ease;
}

/* Form group animations with stagger */
.form-group {
  animation: fadeInUp 0.6s ease-out both;
}

.form-group:nth-child(1) { animation-delay: 0.1s; }
.form-group:nth-child(2) { animation-delay: 0.2s; }
.form-group:nth-child(3) { animation-delay: 0.3s; }
.form-group:nth-child(4) { animation-delay: 0.4s; }

/* Enhanced gradient text effect */


@keyframes textShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
</style>