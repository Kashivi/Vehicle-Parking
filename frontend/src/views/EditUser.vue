<template>
  <div class="edit-profile">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Edit Profile Container -->
    <div class="edit-profile-container">
      <!-- Header Section -->
      <div class="edit-profile-header">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
          </svg>
        </div>
        <h1 class="edit-profile-title">
          <span class="gradient-text">Edit Your Profile</span>
        </h1>
        <p class="edit-profile-subtitle">Update your account information</p>
      </div>

      <!-- Edit Profile Form -->
      <form @submit.prevent="updateUser" class="edit-profile-form">
        <!-- Username (Read-only) -->
        <div class="form-group">
          <label for="username" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            Username
            <span class="readonly-badge">Read-only</span>
          </label>
          <div class="input-wrapper">
            <input 
              type="text" 
              id="username"
              :value="user.username" 
              disabled 
              class="form-input readonly-input"
            />
            <div class="input-border disabled-border"></div>
          </div>
        </div>

        <!-- Email -->
        <div class="form-group">
          <label for="email" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
              <polyline points="22,6 12,13 2,6"/>
            </svg>
            Email Address
          </label>
          <div class="input-wrapper">
            <input 
              type="email" 
              id="email"
              v-model="form.email" 
              placeholder="Update your email address" 
              required 
              class="form-input"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Phone Number -->
        <div class="form-group">
          <label for="phone_number" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
            </svg>
            Phone Number
          </label>
          <div class="input-wrapper">
            <input 
              type="text" 
              id="phone_number"
              v-model="form.phone_number" 
              placeholder="Update your phone number" 
              required 
              class="form-input"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Password -->
        <div class="form-group">
          <label for="password" class="form-label">
            <svg class="label-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <circle cx="12" cy="16" r="1"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            New Password
          </label>
          <div class="input-wrapper">
            <input 
              type="password" 
              id="password"
              v-model="form.password" 
              placeholder="Enter new password" 
              required 
              class="form-input"
            />
            <div class="input-border"></div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="button-group">
          <button type="submit" class="btn-save">
            <span class="btn-content">
              <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/>
                <polyline points="17,21 17,13 7,13 7,21"/>
                <polyline points="7,3 7,8 15,8"/>
              </svg>
              Save Changes
            </span>
            <div class="btn-shimmer"></div>
          </button>
          
          <router-link to="/user-dashboard" class="btn-cancel">
            <span class="btn-content">
              <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 6 6 18"/>
                <path d="M6 6l12 12"/>
              </svg>
              Cancel
            </span>
          </router-link>
        </div>
      </form>

      <!-- Decorative Elements -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EditProfileView',
  data() {
    return {
      user: { id: null, username: '', email: '', phone_number: '' },
      form: { email: '', phone_number: '', password: '' }
    }
  },
  created() {
    const item = localStorage.getItem('user')
    if (!item) {
      alert('No user info found. Please log in again.')
      return this.$router.push('/login')
    }
    const u = JSON.parse(item)
    this.user = u
    this.form.email = u.email
    this.form.phone_number = u.phone_number
  },
  methods: {
    async updateUser() {
      try {
        const payload = {
          user_id: this.user.user_id,
          email: this.form.email,
          phone_number: this.form.phone_number,
          password: this.form.password
        }

        console.log('Sending payload:', payload)
        const res = await fetch('http://localhost:5000/api/userinfo', {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        })
        console.log('HTTP status:', res.status, 'Content-Type header:', res.headers.get('Content-Type'));

        const json = await res.json()
        if (res.ok && json.status === 'ok') {
          alert('User updated successfully')
          const updated = { ...this.user, ...{ email: this.form.email, phone_number: this.form.phone_number } }
          localStorage.setItem('user', JSON.stringify(updated))
          this.$router.push('/user-dashboard')
        } else {
          alert(`Update failed (${res.status}): ${json.message}`)
        }
      } catch (e) {
        console.error(e)
        alert('Network or server error')
      }
    }
  }
}
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

.edit-profile {
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

/* Edit Profile Container */
.edit-profile-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 480px;
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
.edit-profile-header {
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

.edit-profile-title {
  font-size: 2.4em;
  font-weight: 800;
  margin-bottom: 8px;
  letter-spacing: -1px;
}

.gradient-text {
  background: linear-gradient(135deg, 
    var(--accent-orange) 0%, 
    var(--pink-accent) 30%, 
    var(--accent-purple) 60%, 
    var(--primary-blue) 100%);
  background-size: 300% 300%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: textShimmer 4s ease-in-out infinite;
}

@keyframes textShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.edit-profile-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

/* Form Styling */
.edit-profile-form {
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 25px;
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
  width: 18px;
  height: 18px;
  color: var(--accent-orange);
  transition: all 0.3s ease;
}

.readonly-badge {
  background: linear-gradient(135deg, var(--medium-gray), var(--light-gray));
  color: var(--white);
  font-size: 0.7em;
  padding: 2px 8px;
  border-radius: 10px;
  margin-left: auto;
  font-weight: 500;
}

.input-wrapper {
  position: relative;
}

.form-input {
  width: 100%;
  padding: 16px 20px;
  border: 2px solid transparent;
  border-radius: 12px;
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--accent-orange), var(--pink-accent), var(--accent-purple)) border-box;
  font-size: 1em;
  transition: all 0.3s ease;
  box-shadow: 0 4px 20px var(--shadow);
  outline: none;
  position: relative;
  z-index: 2;
}

.readonly-input {
  background: linear-gradient(var(--light-gray), var(--light-gray)) padding-box,
              linear-gradient(135deg, var(--medium-gray), var(--light-gray)) border-box;
  color: var(--medium-gray);
  cursor: not-allowed;
}

.form-input:focus:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(245, 158, 11, 0.3);
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--primary-blue)) border-box;
}

.form-input::placeholder {
  color: var(--medium-gray);
  opacity: 0.7;
}

.input-border {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--success-green), var(--cyan-accent), var(--primary-blue));
  border-radius: 0 0 12px 12px;
  transition: width 0.3s ease;
}

.disabled-border {
  background: var(--medium-gray);
}

.form-input:focus:not(:disabled) + .input-border {
  width: 100%;
}

/* Button Group */
.button-group {
  display: flex;
  gap: 15px;
  margin-top: 35px;
}

/* Save Button */
.btn-save {
  flex: 2;
  padding: 18px 24px;
  background: linear-gradient(135deg, 
    var(--success-green) 0%, 
    var(--cyan-accent) 50%, 
    var(--primary-blue) 100%);
  background-size: 300% 300%;
  color: var(--white);
  border: none;
  border-radius: 12px;
  font-size: 1.1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);
  animation: buttonGlow 3s ease-in-out infinite;
  text-decoration: none;
}

/* Cancel Button */
.btn-cancel {
  flex: 1;
  padding: 18px 24px;
  background: linear-gradient(135deg, 
    var(--medium-gray) 0%, 
    var(--dark-gray) 100%);
  color: var(--white);
  border: none;
  border-radius: 12px;
  font-size: 1.1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(107, 114, 128, 0.3);
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

@keyframes buttonGlow {
  0%, 100% { 
    background-position: 0% 50%;
    box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);
  }
  50% { 
    background-position: 100% 50%;
    box-shadow: 0 10px 40px rgba(6, 182, 212, 0.6);
  }
}

.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 20px;
  height: 20px;
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
    rgba(255, 255, 255, 0.2), 
    transparent);
  transition: left 0.6s ease;
  z-index: 1;
}

.btn-save:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 60px rgba(6, 182, 212, 0.7);
  background-position: 100% 50%;
}

.btn-cancel:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 60px rgba(107, 114, 128, 0.5);
  background: linear-gradient(135deg, 
    var(--dark-gray) 0%, 
    var(--medium-gray) 100%);
}

.btn-save:hover .btn-shimmer {
  left: 100%;
}

.btn-save:hover .btn-icon,
.btn-cancel:hover .btn-icon {
  transform: translateX(3px);
}

.btn-save:active,
.btn-cancel:active {
  transform: translateY(-1px);
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
  width: 60px;
  height: 60px;
  top: 10%;
  right: 10%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatShape 8s ease-in-out infinite;
}

.shape-2 {
  width: 40px;
  height: 40px;
  bottom: 20%;
  left: 15%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatShape 6s ease-in-out infinite reverse;
}

.shape-3 {
  width: 80px;
  height: 80px;
  top: 60%;
  right: 20%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatShape 10s ease-in-out infinite;
}

@keyframes floatShape {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(20px, -15px) rotate(90deg); }
  50% { transform: translate(-10px, -25px) rotate(180deg); }
  75% { transform: translate(-20px, 10px) rotate(270deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .edit-profile-container {
    padding: 40px 30px;
    margin: 10px;
    max-width: 380px;
  }
  
  .edit-profile-title {
    font-size: 2em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
  
  .button-group {
    flex-direction: column;
  }
  
  .btn-save,
  .btn-cancel {
    flex: none;
  }
}

@media (max-width: 480px) {
  .edit-profile-container {
    padding: 30px 20px;
  }
  
  .edit-profile-title {
    font-size: 1.8em;
  }
  
  .form-input {
    padding: 14px 16px;
  }
  
  .btn-save,
  .btn-cancel {
    padding: 16px 20px;
  }
}

/* Focus States for Accessibility */
.btn-save:focus,
.btn-cancel:focus,
.form-input:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Loading State */
.btn-save:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  animation: none;
}

/* Form Animation */
.edit-profile-form {
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Interactive Hover Effects */
.edit-profile-container:hover .parking-icon {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}

.form-group:hover .label-icon {
  color: var(--pink-accent);
  transform: scale(1.1);
  transition: all 0.3s ease;
}

/* Special styling for readonly field */
.form-group:has(.readonly-input):hover .label-icon {
  color: var(--medium-gray);
  transform: scale(1.05);
}
</style>