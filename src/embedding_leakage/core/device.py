"""Optional PyTorch device discovery."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DeviceInfo:
    name: str
    cuda_available: bool
    cuda_device: str | None = None


def detect_device() -> DeviceInfo:
    """Return PyTorch device information without requiring PyTorch."""
    try:
        import torch
    except ImportError:
        return DeviceInfo(name="cpu", cuda_available=False)

    available = torch.cuda.is_available()
    cuda_name = torch.cuda.get_device_name(0) if available else None
    return DeviceInfo(
        name="cuda" if available else "cpu",
        cuda_available=available,
        cuda_device=cuda_name,
    )
