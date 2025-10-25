# CAD/UE Stub API Documentation

## Endpoint: `/stub/generate`
- **Method**: POST
- **Description**: Accepts a JSON specification and returns a preview URL for the generated asset.

### Input Format
JSON object with the following structure:
```json
{
  "type": "string"  // Supported values: "cube", "chair", "gear", "room"
}
```
- `type`: Specifies the asset type. Defaults to "cube" if not provided or invalid.

### Output Format
JSON object:
```json
{
  "preview_url": "string"  // URL path to the asset file, e.g., "/assets/cube.glb"
}
```

### Examples
- Input: `{"type": "cube"}` → Output: `{"preview_url": "/assets/cube.glb"}`
- Input: `{"type": "gear"}` → Output: `{"preview_url": "/assets/gear.glb"}`

### Static Assets
Assets are served at `/assets/{filename}`. Current placeholders:
- cube.glb
- chair.glb
- gear.glb
- room.glb

For integration with Yash's frontend viewer, use the `preview_url` to load and display the asset.