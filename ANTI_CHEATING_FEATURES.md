# Anti-Cheating Features Documentation

## Overview

The Online Examination System now includes comprehensive anti-cheating features designed to detect and prevent various forms of academic dishonesty during exams. These features monitor student behavior in real-time and automatically record violations for administrative review.

## Features Implemented

### 1. Tab Switch Detection
- **Detection Method**: Uses the `visibilitychange` event to detect when students switch browser tabs
- **Real-time Monitoring**: Continuously monitors tab visibility state
- **Automatic Recording**: Violations are automatically logged with timestamp and details
- **Visual Warning**: Students see a warning banner when violations are detected

### 2. Window Focus Monitoring
- **Detection Method**: Monitors `window.focus` and `window.blur` events
- **Application Switching**: Detects when students switch to other applications
- **Mouse Tracking**: Monitors when mouse leaves the exam window area
- **Periodic Checks**: Performs regular focus checks every second

### 3. Copy-Paste Prevention
- **Event Blocking**: Prevents copy, paste, and cut operations
- **Right-click Disabling**: Disables context menu access
- **Keyboard Shortcut Prevention**: Blocks common shortcuts like Ctrl+C, Ctrl+V, Ctrl+X
- **Function Key Blocking**: Disables F1-F12 keys and other system keys

### 4. Fullscreen Enforcement
- **Required Mode**: Students must take exams in fullscreen mode
- **Automatic Detection**: Monitors fullscreen state across different browsers
- **User Prompt**: Provides easy button to enter fullscreen mode
- **Continuous Monitoring**: Tracks fullscreen changes throughout the exam

### 5. Drag and Drop Prevention
- **File Transfer Blocking**: Prevents file drag and drop operations
- **Text Selection Limiting**: Restricts text selection capabilities

## Technical Implementation

### Database Schema

```python
class CheatingAttempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=50, choices=[
        ('TAB_SWITCH', 'Tab Switch'),
        ('WINDOW_FOCUS_LOSS', 'Window Focus Loss'),
        ('COPY_PASTE', 'Copy Paste Attempt'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
```

### JavaScript Monitoring

The anti-cheating system uses comprehensive JavaScript monitoring:

```javascript
// Tab visibility monitoring
document.addEventListener('visibilitychange', handleVisibilityChange);

// Window focus monitoring
window.addEventListener('focus', handleWindowFocus);
window.addEventListener('blur', handleWindowBlur);

// Copy-paste prevention
document.addEventListener('copy', preventCopyPaste);
document.addEventListener('paste', preventCopyPaste);
document.addEventListener('cut', preventCopyPaste);

// Right-click prevention
document.addEventListener('contextmenu', preventRightClick);

// Keyboard shortcut prevention
document.addEventListener('keydown', preventKeyboardShortcuts);
```

### Server-Side Processing

Violations are reported to the server via AJAX requests:

```python
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def report_cheating_view(request):
    """Handle cheating violation reports from JavaScript"""
    if request.method == 'POST':
        data = json.loads(request.body)
        violation_type = data.get('violation_type')
        course_id = request.COOKIES.get('course_id')
        
        if course_id and violation_type:
            course = QMODEL.Course.objects.get(id=course_id)
            student = models.Student.objects.get(user_id=request.user.id)
            
            CheatingAttempt.objects.create(
                student=student,
                exam=course,
                violation_type=violation_type,
                description=data.get('description', '')
            )
```

## User Interface Features

### Student Experience

1. **Security Notice**: Clear warning about monitoring before exam starts
2. **Real-time Warnings**: Visual alerts when violations are detected
3. **Violation Counter**: Shows number of violations during exam
4. **Fullscreen Prompt**: Easy fullscreen mode activation
5. **Warning Banners**: Prominent violation notifications

### Administrator Interface

1. **Dashboard Statistics**: Overview of total violations
2. **Recent Violations**: Latest security incidents
3. **Detailed Reports**: Complete violation history
4. **Filtering Options**: Search by student, exam, or violation type
5. **Management Tools**: Delete false positives

## Security Measures

### Prevention Techniques

1. **Event Prevention**: Blocks prohibited actions before they occur
2. **Real-time Monitoring**: Continuous surveillance during exams
3. **Automatic Logging**: All violations are recorded automatically
4. **Visual Feedback**: Immediate warnings to deter violations
5. **Fullscreen Enforcement**: Reduces access to other applications

### Detection Capabilities

1. **Tab Switching**: Detects browser tab changes
2. **Application Switching**: Monitors window focus changes
3. **Copy-Paste Attempts**: Blocks text copying and pasting
4. **Keyboard Shortcuts**: Prevents system-level shortcuts
5. **Mouse Behavior**: Tracks suspicious mouse movements

## Administrative Features

### Dashboard Integration

- **Violation Statistics**: Total count displayed on admin dashboard
- **Recent Incidents**: Latest violations shown in overview
- **Quick Access**: Direct link to detailed violation reports
- **Real-time Updates**: Statistics update automatically

### Management Tools

- **View All Violations**: Complete list with filtering options
- **Delete Records**: Remove false positive entries
- **Export Capabilities**: Download violation reports
- **Student Tracking**: Monitor individual student behavior

## Browser Compatibility

The anti-cheating system is designed to work across major browsers:

- **Chrome**: Full support for all features
- **Firefox**: Full support for all features
- **Safari**: Full support for all features
- **Edge**: Full support for all features

## Limitations and Considerations

### Technical Limitations

1. **Browser Extensions**: Some browser extensions may interfere
2. **System-Level Access**: Cannot prevent all system shortcuts
3. **Mobile Devices**: Limited functionality on mobile browsers
4. **Network Issues**: Requires stable internet connection for reporting

### Privacy Considerations

1. **Data Collection**: Only violation data is collected
2. **No Screen Recording**: System does not record screens
3. **Minimal Tracking**: Only tracks specific violation events
4. **Data Retention**: Administrators control data retention

## Usage Instructions

### For Students

1. **Read Security Rules**: Review all security requirements before starting
2. **Enter Fullscreen**: Click the fullscreen button when prompted
3. **Stay Focused**: Keep the exam window active throughout
4. **Follow Guidelines**: Avoid prohibited actions during the exam
5. **Report Issues**: Contact administrators for technical problems

### For Administrators

1. **Monitor Dashboard**: Check violation statistics regularly
2. **Review Reports**: Examine detailed violation logs
3. **Manage Records**: Delete false positive entries
4. **Investigate Incidents**: Follow up on suspicious patterns
5. **Update Policies**: Adjust security settings as needed

## Testing and Validation

### Test Script

A comprehensive test script is included (`test_anti_cheating.py`) to verify:

- Model creation and relationships
- Database queries and filtering
- Violation recording functionality
- System integration

### Manual Testing

To test the system manually:

1. Start an exam as a student
2. Attempt to switch tabs (should trigger violation)
3. Try to copy-paste text (should be blocked)
4. Switch to other applications (should be detected)
5. Check admin dashboard for recorded violations

## Future Enhancements

### Planned Features

1. **Advanced Analytics**: Machine learning for pattern detection
2. **Screenshot Detection**: Identify suspicious image content
3. **Audio Monitoring**: Detect background conversations
4. **Device Monitoring**: Track multiple device usage
5. **Behavioral Analysis**: Learn normal student patterns

### Integration Opportunities

1. **LMS Integration**: Connect with learning management systems
2. **Proctoring Services**: Integrate with third-party proctoring
3. **Analytics Platforms**: Export data to analytics tools
4. **Notification Systems**: Real-time alerts for administrators

## Support and Maintenance

### Troubleshooting

1. **False Positives**: Review and delete incorrect violations
2. **Technical Issues**: Check browser compatibility
3. **Performance**: Monitor system performance impact
4. **Updates**: Keep system updated for latest features

### Documentation

- **User Guides**: Detailed instructions for all users
- **Technical Docs**: Implementation and API documentation
- **Best Practices**: Recommended security configurations
- **FAQ**: Common questions and solutions

## Conclusion

The anti-cheating system provides comprehensive protection against common forms of academic dishonesty while maintaining a user-friendly experience. The system balances security with usability, providing administrators with detailed insights while ensuring students can focus on their exams without unnecessary distractions.

For questions or support, please contact the system administrators or refer to the technical documentation. 