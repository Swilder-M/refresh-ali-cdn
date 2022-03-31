# refresh-ali-cdn

## Usage
```yaml
    - name: refresh cdn cache
      uses: Swilder-M/refresh-ali-cdn@v1
      with:
        access_key_id: ${{ secrets.ALI_ACCESS_KEY_ID }}
        access_key_secret: ${{ secrets.ALI_ACCESS_KEY_SECRET }}
        file_paths:
          https://example.com/path/
          https://example.com/path/test.html
```
