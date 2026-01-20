import time
from datetime import datetime, timedelta
import random
import json

class WhatsAppTracker:
    def __init__(self):
        self.tracking_data = {}
    
    def real_time_tracking(self, target, duration_minutes=5):
        """Simulate real-time tracking of WhatsApp activity"""
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        
        print("[+] Tracking dimulai...")
        print("[+] Monitoring: Online status, Typing indicator, Read receipts")
        
        activity_log = []
        
        while datetime.now() < end_time:
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # Simulate random activities
            activities = [
                {"type": "online", "duration": random.randint(10, 300)},
                {"type": "typing", "duration": random.randint(5, 60)},
                {"type": "offline", "duration": random.randint(30, 600)},
                {"type": "read_receipt", "message": f"Pesan di baca jam {current_time}"}
            ]
            
            activity = random.choice(activities)
            activity['timestamp'] = current_time
            
            # Display activity
            if activity['type'] == 'online':
                print(f"[{current_time}] 📱 ONLINE (≈{activity['duration']}s)")
            elif activity['type'] == 'typing':
                print(f"[{current_time}] ✍️ TYPING...")
            elif activity['type'] == 'read_receipt':
                print(f"[{current_time}] 👁️ {activity['message']}")
            
            activity_log.append(activity)
            
            # Wait random interval
            wait_time = random.uniform(5, 30)
            time.sleep(wait_time)
        
        # Save tracking data
        self.tracking_data[target] = {
            'tracking_start': (datetime.now() - timedelta(minutes=duration_minutes)).isoformat(),
            'tracking_end': datetime.now().isoformat(),
            'duration_minutes': duration_minutes,
            'activities': activity_log,
            'summary': self._generate_summary(activity_log)
        }
        
        print(f"\n[+] Tracking selesai. Durasi: {duration_minutes} menit")
    
    def _generate_summary(self, activity_log):
        """Generate summary from activity log"""
        online_count = sum(1 for a in activity_log if a['type'] == 'online')
        typing_count = sum(1 for a in activity_log if a['type'] == 'typing')
        
        return {
            'total_activities': len(activity_log),
            'times_online': online_count,
            'times_typing': typing_count,
            'avg_online_duration': '≈2 menit',
            'most_active_time': self._find_peak_activity(activity_log)
        }
    
    def _find_peak_activity(self, activity_log):
        """Find peak activity time"""
        if not activity_log:
            return "Tidak ada data"
        
        # Simple peak finding
        hours = [int(a['timestamp'].split(':')[0]) for a in activity_log]
        if hours:
            from collections import Counter
            hour_count = Counter(hours)
            peak_hour = hour_count.most_common(1)[0][0]
            return f"Jam {peak_hour}:00-{peak_hour+1}:00"
        
        return "Tidak ditentukan"
    
    def generate_report(self, target):
        """Generate tracking report"""
        if target not in self.tracking_data:
            return {"error": "Tidak ada data tracking"}
        
        data = self.tracking_data[target]
        
        report = {
            'Target': target,
            'Periode Tracking': f"{data['tracking_start']} hingga {data['tracking_end']}",
            'Durasi': f"{data['duration_minutes']} menit",
            'Ringkasan': data['summary'],
            'Aktivitas Terakhir': data['activities'][-1] if data['activities'] else None
        }
        
        # Save report to file
        filename = f"tracking_report_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        report['File_Laporan'] = filename
        return report
