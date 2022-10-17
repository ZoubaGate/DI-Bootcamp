from django import forms

def validate_name(name):
    if (name.isalpha() == False):
        print("invalid name")
        return (f'the name {name} is invalide')
    

class GifForm(forms.Form):
    uploader_name = forms.CharField(
        required=False, min_length=3,
        validators=[validate_name],
        widget=forms.TextInput(
                attrs = {
                        'placeholder': 'write your name here',
                        'style': 'width: 300px;'
                }
            )
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'placeholder':'write a title',
                'style': 'width: 300px;'
            }
        )
    )
    url = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'write a url',
            'style': 'width:300px;'
            }
            
        )
    )
    Category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'write a url',
                'style': 'width:300px;'
            }
            
        )
    )
    
    
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )