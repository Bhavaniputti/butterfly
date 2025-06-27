from tensorflow.keras.preprocessing.image import ImageDataGenerator
from model.model_builder import build_model
import json

def load_data(image_size=(100, 100), batch_size=32):
    base_dir = "data/ButterflyData"

    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )

    train_data = datagen.flow_from_directory(
        base_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='sparse',
        subset='training'
    )

    val_data = datagen.flow_from_directory(
        base_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='sparse',
        subset='validation'
    )

    return train_data, val_data

def main():
    train_data, val_data = load_data()
    print("✅ Class mapping used during training:")
    print(train_data.class_indices)

    with open("class_indices.json", "w") as f:
        json.dump(train_data.class_indices, f)

    model = build_model(num_classes=len(train_data.class_indices))
    model.fit(train_data, epochs=10, validation_data=val_data)
    model.save("butterfly_classifier.h5")
    print("✅ Model trained and saved as butterfly_classifier.h5")

if __name__ == '__main__':
    main()
