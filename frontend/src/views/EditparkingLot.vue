<template>
  <div class="edit-lot">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Main Container -->
    <div class="edit-container">
      <!-- Header Section -->
      <div class="header-section">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
            <!-- Edit Icon -->
            <path d="M75 15 L85 25 L80 30 L70 20 Z" fill="currentColor" opacity="0.8"/>
            <line x1="85" y1="25" x2="90" y2="30" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <h2 class="page-title">
          <span class="gradient-text">Edit Parking Lot</span>
        </h2>
        <p class="page-subtitle">Update lot pricing and capacity</p>
      </div>

      <!-- Form Section -->
      <div class="form-section">
        <div class="info-card">
          <div class="card-header">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
            </svg>
            <h3>Parking Lot Details</h3>
          </div>
          
          <form @submit.prevent="updateLot" class="edit-form">
            <div class="form-grid">
              <!-- Read-only Location -->
              <div class="form-group readonly-group">
                <label for="location_name" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                    <circle cx="12" cy="10" r="3"/>
                  </svg>
                  Location Name
                </label>
                <div class="input-wrapper readonly-wrapper">
                  <input 
                    type="text" 
                    id="location_name"
                    class="form-input readonly-input" 
                    :value="lot.prime_location_name" 
                    readonly 
                  />
                  <div class="input-accent location-accent"></div>
                  <div class="readonly-badge">Read Only</div>
                </div>
              </div>

              <!-- Read-only Address -->
              <div class="form-group readonly-group">
                <label for="address" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                    <polyline points="9,22 9,12 15,12 15,22"/>
                  </svg>
                  Address
                </label>
                <div class="input-wrapper readonly-wrapper">
                  <textarea 
                    id="address"
                    class="form-textarea readonly-input" 
                    rows="3"
                    :value="lot.address" 
                    readonly
                  ></textarea>
                  <div class="input-accent address-accent"></div>
                  <div class="readonly-badge">Read Only</div>
                </div>
              </div>

              <!-- Editable Price -->
              <div class="form-group editable-group">
                <label for="price" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="12" y1="1" x2="12" y2="23"/>
                    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                  </svg>
                  Price per Hour (₹)
                </label>
                <div class="input-wrapper editable-wrapper">
                  <input
                    type="number"
                    id="price"
                    class="form-input editable-input"
                    v-model.number="form.price"
                    required
                    min="1"
                    step="1"
                  />
                  <div class="input-accent price-accent"></div>
                  <div class="currency-symbol">₹</div>
                </div>
              </div>

              <!-- Editable Number of Spots -->
              <div class="form-group editable-group">
                <label for="spots" class="form-label">
                  <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                    <path d="M9 9h6v6H9z"/>
                  </svg>
                  Number of Spots
                </label>
                <div class="input-wrapper editable-wrapper">
                  <input
                    type="number"
                    id="spots"
                    class="form-input editable-input"
                    v-model.number="form.number_of_spots"
                    required
                    min="1"
                    step="1"
                  />
                  <div class="input-accent spots-accent"></div>
                  <div class="spots-indicator">{{ form.number_of_spots || 0 }} spots</div>
                </div>
              </div>
            </div>

            <div class="button-group">
              <button type="submit" class="btn btn-save">
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="9,11 12,14 22,4"/>
                    <path d="M21,12v7a2,2 0 0,1 -2,2H5a2,2 0 0,1 -2,-2V5a2,2 0 0,1 2,-2h11"/>
                  </svg>
                  Save Changes
                </span>
                <div class="btn-shimmer"></div>
              </button>
              
              <router-link to="/admin-dashboard" class="btn btn-cancel">
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                  Cancel
                </span>
              </router-link>
            </div>
          </form>
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
  name: 'EditLot',
  data() {
    return {
      lot: {
        prime_location_name: '',
        address: '',
        price: 0,
        number_of_spots: 0
      },
      form: {
        price: 0,
        number_of_spots: 0
      },
      lotId: null
    };
  },
  async created() {
    this.lotId = this.$route.params.id;
    await this.loadLot();
  },
  methods: {
    async loadLot() {
      try {
        const res = await fetch('http://localhost:5000/api/parkinglot');
        const data = await res.json();
        const found = Array.isArray(data.lots)
          ? data.lots.find(item => item.id === +this.lotId)
          : null;
        if (!found) throw new Error('Lot not found');
        
        this.lot = found;
        this.form.price = found.price;
        this.form.number_of_spots = found.number_of_spots;
      } catch (e) {
        alert(e.message);
        this.$router.push('/admin-dashboard');
      }
    },
    async updateLot() {
      const saveBtn = document.querySelector('.btn-save');
      if (saveBtn) {
        saveBtn.disabled = true;
        const btnContent = saveBtn.querySelector('.btn-content');
        if (btnContent) {
          btnContent.innerHTML = `
            <svg class="btn-icon spinner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 12a9 9 0 11-6.219-8.56"/>
            </svg>
            Updating...
          `;
        }
      }

      try {
        const res = await fetch('http://localhost:5000/api/parkinglot', {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            id: this.lotId,
            price: this.form.price,
            number_of_spots: this.form.number_of_spots
          })
        });
        
        const json = await res.json();
        
        if (json.status === 'ok') {
          alert('✅ Lot updated successfully!');
          this.$router.push('/admin-dashboard');
        } else {
          alert(`❌ Update failed: ${json.message}`);
        }
      } catch (e) {
        console.error('Update error:', e);
        alert('⚠️ Network or server error');
      } finally {
        if (saveBtn) {
          saveBtn.disabled = false;
          const btnContent = saveBtn.querySelector('.btn-content');
          if (btnContent) {
            btnContent.innerHTML = `
              <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9,11 12,14 22,4"/>
                <path d="M21,12v7a2,2 0 0,1 -2,2H5a2,2 0 0,1 -2,-2V5a2,2 0 0,1 2,-2h11"/>
              </svg>
              Save Changes
            `;
          }
        }
      }
    }
  }
};
</script>

<style scoped>
/* Color Variables - Same as other components */
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

.edit-lot {
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
.edit-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 800px;
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
  color: #000;
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}

.page-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

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

/* Info Card */
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
  color: var(--primary-blue);
}

.card-header h3 {
  margin: 0;
  font-weight: 700;
  color: var(--dark-gray);
}

/* Form Grid */
.form-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 25px;
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
  margin-bottom: 10px;
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
  display: flex;
  align-items: center;
}

.form-input,
.form-textarea {
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
  resize: none;
}

.form-textarea {
  font-family: inherit;
  line-height: 1.5;
}

/* Readonly styling */
.readonly-input {
  background: rgba(243, 244, 246, 0.7) !important;
  color: var(--medium-gray) !important;
  cursor: not-allowed;
  border-color: rgba(107, 114, 128, 0.3) !important;
}

.readonly-wrapper {
  position: relative;
}

.readonly-badge {
  position: absolute;
  top: -8px;
  right: 12px;
  background: linear-gradient(135deg, var(--medium-gray), var(--dark-gray));
  color: var(--white);
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.7em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Editable styling */
.editable-input:focus {
  border-color: transparent;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.2);
}

.currency-symbol,
.spots-indicator {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: var(--accent-orange);
  color: var(--white);
  padding: 8px 12px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 0.9em;
  box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);
}

.spots-indicator {
  background: var(--success-green);
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

/* Input accents */
.input-accent {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 100%;
  border-radius: 0 0 12px 12px;
  opacity: 0.8;
}

.location-accent {
  background: linear-gradient(90deg, var(--success-green), var(--cyan-accent));
}

.address-accent {
  background: linear-gradient(90deg, var(--accent-purple), var(--primary-blue));
}

.price-accent {
  background: linear-gradient(90deg, var(--accent-orange), var(--pink-accent));
}

.spots-accent {
  background: linear-gradient(90deg, var(--cyan-accent), var(--success-green));
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
  text-decoration: none;
  display: inline-block;
  text-align: center;
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

.spinner-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.btn-save {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);
}

.btn-save:hover:not(:disabled) {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 60px rgba(16, 185, 129, 0.6);
}

.btn-save:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  animation: none;
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

.btn-shimmer {
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

.btn:hover .btn-shimmer {
  left: 100%;
}

.btn:hover .btn-icon {
  transform: scale(1.1);
}

.btn:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
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

/* Animations */
.form-section {
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

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

/* Interactive Effects */
.form-group:hover .label-icon {
  color: var(--accent-orange);
  transform: scale(1.1);
  transition: all 0.3s ease;
}

.editable-group:hover .form-input,
.editable-group:hover .form-textarea {
  border-color: var(--accent-orange);
}

/* Responsive Design */
@media (max-width: 768px) {
  .edit-container {
    padding: 40px 25px;
    margin: 10px;
  }
  
  .page-title {
    font-size: 2em;
  }
  
  .button-group {
    flex-direction: column;
    align-items: center;
  }
  
  .btn {
    width: 100%;
    max-width: 280px;
  }
}

@media (max-width: 480px) {
  .edit-container {
    padding: 30px 20px;
  }
  
  .page-title {
    font-size: 1.8em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .currency-symbol,
  .spots-indicator {
    position: relative;
    right: auto;
    top: auto;
    transform: none;
    margin-top: 8px;
    display: inline-block;
  }
}

/* Enhanced Focus States */
.editable-input:focus + .input-accent {
  height: 4px;
  opacity: 1;
  animation: accentGlow 2s ease infinite;
}

@keyframes accentGlow {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 1; }
}

/* Loading States */
.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  animation: none;
}

/* Success and Error States */
.form-input.success {
  border-color: var(--success-green);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.form-input.error {
  border-color: var(--red-accent);
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

/* Tooltip styling for readonly fields */
.readonly-wrapper::after {
  content: 'This field cannot be modified';
  position: absolute;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--dark-gray);
  color: var(--white);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 0.8em;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.readonly-wrapper:hover::after {
  opacity: 1;
}
</style>